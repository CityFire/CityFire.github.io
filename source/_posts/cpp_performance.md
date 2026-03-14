---
title: C++语言特性性能分析
--- 
## 一、C++语言特性性能分析简介
通常大多数开发人员认为，汇编语言和C语言比较适合编写对性能要求非常高的程序，C++语言主要适用于编写复杂度非常高但性能要求并不是很高的程序。因为大多数开发人员认为，C++语言设计时因为考虑到支持多种编程模式（如面向对象编程和范型编程）以及异常处理等，从而引入了太多新的语言特性。新的语言特性往往使得C++编译器在编译程序时插入了很多额外的代码，会导致最终生成的二进制代码体积膨胀，而且执行速度下降。

但事实并非如此，通常一个程序的速度在框架设计完成时大致已经确定，而并非因为采用C++语言才导致速度没有达到预期目标。因此，当一个程序的性能需要提高时，首先需要做的是用性能检测工具对其运行的时间分布进行一个准确的测量，找出关键路径和真正的性能瓶颈所在，然后针对性能瓶颈进行分析和优化，而不是主观地将性能问题归咎于程序所采用的语言。工程实践表明，如果框架设计不做修改，即使使用C语言或汇编语言重新改写，也并不能保证提高总体性能。

因此，遇到性能问题时，首先应检查和反思程序的总体架构，然后使用性能检测工具对其实际运行做准确的测量，再针对性能瓶颈进行分析和优化。

但C++语言中确实有一些操作、特性比其它因素更容易成为程序的性能瓶颈，常见因素如下：

#### （1）缺页

缺页通常意味着要访问外部存储，因为外部存储访问相对于访问内存或代码执行，有数量级的差别。因此，只要有可能，应该尽量想办法减少缺页。

#### （2）从堆中动态申请和释放内存

C语言中的malloc/free和C++语言中的new/delete操作时非常耗时的，因此要尽可能优先考虑从线程栈中获取内存。优先考虑栈而减少从动态堆中申请内存，不仅因为在堆中分配内存比在栈中要慢很多，而且还与尽量减少缺页有关。当程序执行时，当前栈帧空间所在的内存页肯定在物理内存中，因此程序代码对其中变量的存取不会引起缺页；如果从堆空间生成对象，只有指向对象的指针在栈上，对象本身则存储在堆空间中。堆一般不可能都在物理内存中，而且由于堆分配内存的特性，即使两个相邻生成的对象，也很有可能在堆内存位置上相距很远。因此，当访问两个对象时，虽然分别指向两个对象的指针都在栈上，但通过两个指针引用对象时很有可能会引起两次缺页。

#### （3）复杂对象的创建和销毁

复杂对象的创建和销毁会比较耗时，因此对于层次较深的递归调用需要重点关注递归内部的对象创建。其次，编译器生成的临时对象因为在程序的源码中看不到，更不容易察觉，因此需要重点关注。

#### （4）函数调用

由于函数调用有固定的额外开销，因此当函数体的代码量相对较少，并且函数被非常频繁调用时，函数调用时的固定开销容易成为不必要的开销。C语言的宏和C++语言的内联函数都是为了在保持函数调用的模块化特征基础上消除函数调用的固定额外开销而引入的。由于C语言的宏在提供性能优势的同时也给开发和调试带来不便，因此C++语言中推荐使用内联函数。

## 二、构造函数与析构函数
### 1、构造函数与析构函数简介
构造函数和析构函数的特点是当创建对象时自动执行构造函数；当销毁对象时，析构函数自动被执行。构造函数是一个对象最先被执行的函数，在创建对象时调用，用于初始化对象的初始状态和取得对象被使用前需要的一些资源，如文件、网络连接等；析构函数是一个对象最后被执行的函数，用于释放对象拥有的资源。在对象的生命周期内，构造函数和析构函数都只会执行一次。

创建一个对象有两种方式，一种是从线程运行栈中创建，称为局部对象。销毁局部对象并不需要程序显示地调用析构函数，而是当程序运行出对象所属的作用域时自动调用对象的析构函数。

创建对象的另一种方式是从全局堆中动态分配，通常使用new或malloc分配堆空间。

```
    Obejct* p = new Object();//1
    // do something //2
    delete p;//3
    p = NULL;//4
```
执行语句1时，指针p所指向对象的内存从全局堆空间中获得，并将地址赋值给p，p本身是一个局部变量，需要从线程栈中分配，p所指向对象从全局堆中分配内存存放。从全局堆中创建的对象需要显示调用delete进行销毁，delete会调用指针p指向对象的析构函数，并将对象所占的全局堆内存空间返回给全局堆。执行语句3后，指针p指向的对象被销毁，但指针p还存在于栈中，直到程序退出其所在作用域。将p指针所指向对象销毁后，p指针仍指向被销毁对象的全局堆空间位置，此时指针p变成一个悬空指针，此时使用指针p是危险的，通常推荐将p赋值NULL。

在Win32平台，访问销毁对象的全局堆空间内存会导致三种情况：

```
（1）被销毁对象所在的内存页没有任何对象，堆管理器已经将所占堆空间进一步回收给操作系统，此时通过指针访问会引起访问违例，即访问了不合法内存，引起进程崩溃。

（2）被销毁对象所在的内存页存在其它对象，并且被销毁对象曾经占用的全局堆空间被回收后尚未分配给其它对象，此时通过指针p访问取得的值是无意义的，虽然不会立刻引起进程崩溃，但针对指针p的后续操作行为是不可预测的。

（3）被销毁对象所在的内存页存在其它对象，并且被销毁对象曾经占用的全局堆空间被回收后已经分配给其它对象，此时通过指针p取得的值是其它对象，虽然对指针p的访问不会引起进程崩溃，但极有可能引起对象状态的改变。
```

### 2、对象的构造过程
创建一个对象分为两个步骤，即首先取得对象所需的内存（从线程栈或全局堆），然后在内存空间上执行构造函数。在构造函数构建对象时，构造函数也分为两个步骤。第一步执行初始化（通过初始化参数列表），第二步执行构造函数的函数体。

```
class Derived : public Base
{
public:
    Derived(): id(1), name("UnNamed")   // 1
    {
        // do something     // 2
    }
private:
    int id;
    string name;
};
```

语句1中冒号后的代码即为初始化列表，每个初始化单元都是变量名（值）的模式，不同单元之间使用逗号分隔。构造函数首先根据初始化列表执行初始化，然后执行构造函数的函数体（语句2）。初始化操作的注意事项如下：

```
（1）构造函数其实是一个递归操作，在每层递归内部的操作遵循严格的次序。递归模式会首先执行父类的构造函数（父类的构造函数操作也相应包含执行初始化和执行构造函数函数体两个部分），父类构造函数返回后构造类自己的成员变量。构造类自己的成员变量时，一是严格按照成员变量在类中的声明顺序进行，与成员变量在初始化列表中出现的顺序完全无关；二是当有些成员变量或父类对象没有在初始化列表出现时，仍然在初始化操作中对其进行初始化，內建类型成员变量被赋值给一个初值，父类对象和类成员变量对象被调用其默认构造函数初始化，然后父类的构造函数和子成员变量对象在构造函数执行过程中也遵循上述递归操作，直到类的继承体系中所有父类和父类所含的成员变量都被构造完成，类的初始化操作才完成。

（2）父类对象和一些成员变量没有出现在初始化列表中时，其仍然会被执行默认构造函数。因此，相应对象所属类必须提供可以调用的默认构造函数，为此要求相应的类必须显式提供默认构造函数，要么不能阻止编译器隐式生成默认构造函数，定义除默认构造函数外的其它类型的构造函数将会阻止编译器生成默认构造函数。如果编译器在编译时，发现没有可供调用的默认构造函数，并且编译器也无法生成默认构造函数，则编译无法通过。

（3）对两类成员变量，需要强调指出（即常量型和引用型）。由于所有成员变量在执行函数体前已经被构造，即已经拥有初始值，因此，对于常量型和引用型变量必须在初始化列表中正确初始化，而不能将其初始化放在构造函数体内。

（4）初始化列表可能没有完全列出其子成员或父类对象成员，或者顺序与其在类中的声明顺序不同，仍然会保证严格被全部并且严格按照顺序被构建。即程序在进入构造函数体前，类的父类对象和所有子成员变量对象已经被生成和构造。如果在构造函数体内为其执行赋值操作，显然属于浪费。如果在构造函数时已经知道如何为类的子成员变量初始化，则应该将初始化信息通过构造函数的初始化列表赋予子成员变量，而不是在构造函数体内进行初始化，因为进入构造函数时，子成员变量已经初始化一次。
```

### 3、对象的析构过程
析构函数和构造函数一样，是递归的过程，但存在不同。一是析构函数不存在初始化操作部分，析构函数的主要工作就是执行析构函数的函数体；二是析构函数执行的递归与构造函数相反，在每一层递归中，成员变量对象的析构顺序也与构造函数相反。

析构函数只能选择类的成员变量在类中声明的顺序作为析构的顺序参考（正序或逆序）。因为构造函数选择了正序，而析构函数的工作与构造函数相反，因此析构函数选择逆序。又因为析构函数只能使用成员变量在类中的声明顺序作为析构顺序的依据（正序或逆序），因此构造函数也只能选择成员变量在类中的声明顺序作为构造的顺序依据，而不能采用初始化列表的顺序作为顺序依据。

如果操作的对象属于一个复杂继承体系的末端节点，其析构过程也将十分耗时。

在C++程序中，创建和销毁对象是影响性能的一个非常突出的操作。首先，如果是从全局堆空间中生成对象，则需要先进行动态内存分配操作，而动态内存的分配与回收是非常耗时的操作，因为涉及到寻找匹配大小的内存块，找到后可能还需要截断处理，然后还需要修改维护全局堆内存使用情况信息的链表。频繁的内存操作会严重影响性能的下降，使用内存池技术可以减少从全局动态堆空间申请内存的次数，提高程序的总体性能。当取得内存后，如果需要生成的内对象属于复杂继承体系的末端类，则构造函数的调用将会引起一连串的递归构造操作，在大型复杂系统中，大量的此类对象构造将会消耗CPU操作的主要部分。

由于对象的创建和销毁会影响性能，在尽量减少自己代码生成对象的同时，需要关注编译器在编译时临时生成的对象，尽量避免临时对象的生成。

如果在实现构造函数时，在构造函数体中进行了第二次的赋值操作，也会浪费CPU时间。

### 4、函数参数传递
减少对象创建和销毁的常见方法是在声明中将所有的值传递改为常量引用传递，如：

```
int func(Object obj);// 1
int func(const Object& obj);// 2
```

值传递验证示例如下：

```
#include <iostream>
 
using namespace std;
 
class Object
{
public:
    Object(int i = 1)
    {
        n = i;
        cout << "Object(int i = 1): " << endl;
    }
 
    Object(const Object& another)
    {
        n = another.n;
        cout << "Object(const Object& another): " << endl;
    }
 
    void increase()
    {
        n++;
    }
 
    int value()const
    {
        return n;
    }
 
    ~Object()
    {
        cout << "~Object()" << endl;
    }
private:
    int n;
};
 
void func(Object obj)
{
    cout << "enter func, before increase(), n = " << obj.value() << endl;
    obj.increase();
    cout << "enter func, after increase(), n = " << obj.value() << endl;
}
 
int main()
{
    Object a; // 1
    cout << "before call func, n = " << a.value() << endl;
    func(a); // 2
    cout << "after call func, n = " << a.value() << endl;// 3
 
    return 0;
}
 
// output:
//Object(int i = 1): // 4
//before call func, n = 1
//Object(const Object& another): // 5
//enter func, before increase(), n = 1 // 6
//enter func, after increase(), n = 2 // 7
//~Object() // 8
//after call func, n = 1 // 9
//~Object()
```

语句4的输出为语句1处的对象构造，语句5输出则是语句2处的func(a)函数调用，调用开始时通过拷贝构造函数生成对象a的复制品，紧跟着在函数内检查n的输出值输出语句6，输出值与func函数外部元对象a的值相同，然后复制品调用increase函数将n值加1，此时复制品的n值为2，并输出语句7。func函数执行完毕后销毁复制品，输出语句8。main函数内继续执行，打印原对象a的n值为1，输出语句9。

当函数需要修改传入参数时，应该用引用传入参数；当函数不会修改传入参数时，如果函数声明中传入参数为对象，则函数可以达到设计目的，但会生成不必要的复制品对象，从而引入不必要的构造和析构操作，应该使用常量引用传入参数。

构造函数的重复赋值对性能影响验证示例如下：

```
#include <iostream>
#include <time.h>
 
using namespace std;
 
class DArray
{
public:
    DArray(double v = 1.0)
    {
        for(int i = 0; i < 1000; i++)
        {
            d[i] = v + i;
        }
    }
 
    void init(double v = 1.0)
    {
        for(int i = 0; i < 1000; i++)
        {
            d[i] = v + i;
        }
    }
private:
    double d[1000];
};
 
class Object
{
public:
    Object(double v)
    {
        d.init(v);
    }
private:
    DArray d;
};
 
int main()
{
    clock_t start, finish;
    start = clock();
    for(int i = 0; i < 100000; i++)
    {
        Object obj(2.0 + i);
    }
    finish = clock();
    cout << "Used Time: " << double(finish - start) << "" << endl;
 
    return 0;
}
```

耗时为600000单位，如果通过初始化列表对成员变量进行初始化，其代码如下：

```
#include <iostream>
#include <time.h>
 
using namespace std;
 
class DArray
{
public:
    DArray(double v = 1.0)
    {
        for(int i = 0; i < 1000; i++)
        {
            d[i] = v + i;
        }
    }
 
    void init(double v = 1.0)
    {
        for(int i = 0; i < 1000; i++)
        {
            d[i] = v + i;
        }
    }
private:
    double d[1000];
};
 
class Object
{
public:
    Object(double v): d(v)
    {
 
    }
private:
    DArray d;
};
 
int main()
{
    clock_t start, finish;
    start = clock();
    for(int i = 0; i < 100000; i++)
    {
        Object obj(2.0 + i);
    }
 
    finish = clock();
    cout << "Used Time: " << double(finish - start) << "" << endl;
 
    return 0;
}
```

耗时为300000单位，性能提高约50%。

## 三、继承与虚函数
#### 1、虚函数与动态绑定机制
虚函数是C++语言引入的一个重要特性，提供了动态绑定机制，动态绑定机制使得类继承的语义变得相对明晰。

```
（1）基类抽象了通用的数据及操作。对于数据而言，如果数据成员在各个派生类中都需要用到，需要将其声明在基类中；对于操作而语言，如果操作对于各个派生类都有意义，无论其语义是否会被修改和扩展，需要将其声明在基类中。

（2）某些操作，对于各个派生类而言，语义完全保持一致，而无需修改和扩展，则相应操作声明为基类的非虚成员函数。各个派生类在声明为基类的派生类时，默认继承非虚成员函数的声明和实现，如果默认继承基类的数据成员一样，而不必另外做任何声明，构成代码复用。

（3）对于某些操作，虽然对于各个派生类都有意义，但其语义并不相同，则相应的操作应该声明为虚成员函数。各个派生类虽然也继承了虚成员函数的声明和实现，但语义上应该对虚成员函数的实现进行修改或扩展。如果在实现修改、扩展虚成员函数的过程中，需要用到额外的派生类独有的数据时，则将相应的数据声明为派生类自己的数据成员。
```

当更高层次的程序框架（继承体系的使用者）使用此继承体系时，处理的是抽象层次的对象集合，对象集合的成员本质是各种派生类对象，但在处理对象集合的对象时，使用的是抽象层次的操作。高层程序框架并不区分相应操作中哪些操作对于派生类是不变的，哪些操作对于派生类是不同的，当实际执行到各操作时，运行时系统能够识别哪些操作需要用到动态绑定。从而找到对应派生类的修改或扩展的操作版本。即对继承体系的使用者而言，继承体系内部的多样性是透明的，不必关心其继承细节，处理的是一组对使用者而言整体行为一致的对象。即使继承体系内部增加、删除了某个派生类，或某个派生类的虚函数实现发生了改变，使用者的代码也不必做任何修改，使程序的模块化程度得到极大提高，其扩展性、维护性和代码可读性也会提高。对于对象继承体系使用者而言，只看到抽象类型，而不必关心具体是哪种具体类型。

#### 2、虚函数的效率分析
虚函数的动态绑定特性虽然很好，但存在内存空间和时间开销，每个支持虚函数的类（基类或派生类）都会有一个包含其所有支持的虚函数的虚函数表的指针。每个类对象都会隐含一个虚函数表指针（virtual pointer），指向其所属类的虚函数表。当通过基类的指针或引用调用某个虚函数时，系统需要首先定位指针或引用真正对应的对象所隐含的虚函数指针，然后虚函数指针根据虚函数的名称对其所指向的虚函数表进行一个偏移定位，再调用偏移定位处的函数指针对应的虚函数，即动态绑定的解析过程。C++规范只需要编译器能够保证动态绑定的语义，但大多数编译器都采用上述方法实现虚函数。

```
（1）每个支持虚函数的类都有一个虚函数表，虚函数表的大小与类拥有的虚函数的多少成正比。一个程序中，每个类的虚函数表只有一个，与类对象的数量无关。支持虚函数的类的每个类对象都有一个指向类的虚函数表的虚函数指针，因此程序运行时虚函数指针引起的内存开销与生成的类对象数量成正比。

（2）支持虚函数的类生成每个对象时，在构造函数中会调用编译器在构造函数内部插入的初始化代码，来初始化其虚函数指针，使其指向正确的虚函数表。当通过指针或引用调用虚函数时，会根据虚函数指针找到相应类的虚函数表。
```

#### 3、虚函数与内联
内联函数通常可以提高代码执行速度，很多普通函数会根据情况进行内联化，但虚函数无法利用内联化的优势。因为内联是在编译阶段编译器将调用内联函数的位置用内联函数体替代（内联展开），但虚函数本质上是运行期行为。在编译阶段，编译器无法知道某处的虚函数调用在真正执行的时后需要调用哪个具体的实现（即编译阶段无法确定其具体绑定），因此，编译阶段编译器不会对通过指针或引用调用的虚函数进行内联化。如果需要利用虚函数的动态绑定的设计优势，必须放弃内联带来的速度优势。

如果不使用虚函数，可以通过在抽象基类增加一个类型标识成员用于在运行时识别具体的派生类对象，在派生类对象构造时必须指定具体的类型。继承体系的使用者调用函数时不再需要一次间接地根据虚函数表查找虚函数指针的操作，但在调用前仍然需要使用switch语句对其类型进行识别。

因此虚函数的缺点可以认为只有两条，即虚函数表的空间开销以及无法利用内联函数的速度优势。由于每个含有虚函数的类在整个程序只有一个虚函数表，因此虚函数表引起的空间开销时非常小的。所以，可以认为虚函数引入的性能缺陷只是无法利用内联函数。

通常，非虚函数的常规设计假如需要增加一种新的派生类型，或者删除一种不再支持的派生类型，都必须修改继承体系所有使用者的所有与类型相关的函数调用代码。对于一个复杂的程序，某个继承体系的使用者会很多，每次对继承体系的派生类的修改都会波及使用者。因此，不使用虚函数的常规设计增加了代码的耦合度，模块化不强，导致项目的可扩展性、可维护性、代码可读性都会降低。面向对象编程的一个重要目的就是增加程序的可扩展性和可维护性，即当程序的业务逻辑发生改变时，对原有程序的修改非常方便，降低因为业务逻辑改变而对代码修改时出错的概率。

因此，在性能和其它特性的选择方面，需要开发人员根据实际情况进行进行权衡和取舍，如果性能检验确认性能瓶颈不是虚函数没有利用内联的优势引起，可以不必考虑虚函数对性能的影响。

## 四、临时对象
#### 1、临时对象简介
对象的创建与销毁对程序的性能影响很大，尤其是对象的类处于一个复杂继承体系的末端，或者对象包含很多成员对象（包括其所有父类对象，即直接或者间接父类的所有成员变量对象）时，对程序性能影响尤其显著。因此，作为一个对性能敏感的程序员，应该尽量避免创建不必要的对象，以及随后的销毁。除了减少显式地创建对象，也要尽量避免编译器隐式地创建对象，即临时对象。

```
#include <iostream>
#include <cstring>
 
class Matrix
{
public:
    Matrix(double d = 1.0)
    {
        for(int i = 0; i < 10; i++)
        {
            for(int j = 0; j < 10; j++)
            {
                m[i][j] = d;
            }
        }
        cout << "Matrix(double d = 1.0)" << endl;
    }
    Matrix(const Matrix& another)
    {
        cout << "Matrix(const Matrix& another)" << endl;
        memcpy(this, &another, sizeof(another));
    }
 
    Matrix& operator=(const Matrix& another)
    {
        if(this != &another)
        {
            memcpy(this, &another, sizeof(another));
        }
        cout << "Matrix& operator=(const Matrix& another)" << endl;
        return *this;
    }
 
    friend const Matrix operator+(const Matrix& m1, const Matrix& m2);
private:
    double m[10][10];
};
 
const Matrix operator+(const Matrix& m1, const Matrix& m2)
{
    Matrix sum; // 1
    for(int i = 0; i < 10; i++)
    {
        for(int j = 0; j < 10; j++)
        {
            sum.m[i][j] = m1.m[i][j] + m2.m[i][j];
        }
    }
    return sum; // 2
}
 
int main()
{
    Matrix a(2.0), b(3.0), c; // 3
    c = a + b; // 4
    return 0;
}
```

由于GCC编译器默认进行了返回值优化（Return Value Optimization，简称RVO），因此需要指定-fno-elide-constructors选项进行编译：

```
g++ -fno-elide-constructors main.cpp
输出结果如下：

Matrix(double d = 1.0) // 1
Matrix(double d = 1.0) // 2
Matrix(double d = 1.0) // 3
Matrix(double d = 1.0) // 4
Matrix(const Matrix& another) // 5
Matrix& operator=(const Matrix& another) // 6
```
分析代码，语句3生成3个Matrix对象，调用3次构造函数，语句4调用operator+执行到语句1时生成临时变量sum，调用1次构造函数，语句4调用赋值操作，不会生成新的Matrix对象。输出5则是因为a+b调用operator+函数时需要返回一个Matrix变量sum，然后进一步通过operator=函数将sum变量赋值给变量c，但a+b返回时，sum变量已经被销毁，即在operator+函数调用结束时被销毁，其返回的Matrix变量需要在调用a+b函数的栈中开辟空间来存放，临时的Matrix对象是在a+b返回时通过Matrix拷贝构造函数构造，即输出5打印。

如果使用默认GCC编译选项编译，GCC编译器默认会进行返回值优化。

```
g++ main.cpp
程序输出如下：

Matrix(double d = 1.0)
Matrix(double d = 1.0)
Matrix(double d = 1.0)
Matrix(double d = 1.0)
Matrix& operator=(const Matrix& another)
```
临时对象与临时变量并不相同。通常，临时变量是指为了暂时存放某个值的变量，显式出现在源码中；临时对象通常指编译器隐式生成的对象。

临时对象在C++语言中的特征是未出现在源代码中，而是从栈中产生未命名对象，开发人员并没有声明要使用临时对象，由编译器根据情况产生，通常开发人员不会注意到其产生。

返回值优化（Return Value Optimization，简称RVO）是一种优化机制，当函数需要返回一个对象的时候，如果自己创建一个临时对象用户返回，那么临时对象会消耗一个构造函数（Constructor）的调用、一个复制构造函数的调用（Copy Constructor）以及一个析构函数（Destructor）的调用的代价，而如果稍微做一点优化，就可以将成本降低到一个构造函数的代价。

#### 2、临时对象生成
通常，产生临时对象的场合如下：

```
（1）当实际调用函数时传入的参数与函数定义中声明的变量类型不匹配。

（2）当函数返回一个对象时。
```

在函数传递参数为对象时，实际调用时因为函数体内的对象与实际传入的对象并不相同，而是传入对象的拷贝，因此有开发者认为函数体内的拷贝对象也是一个临时对象，但严格来说，函数体内的拷贝对象并不符合未出现在源码中。

对于类型不匹配生成临时对象的情况，示例如下：

```
#include <iostream>
 
using namespace std;
class Rational
{
public:
    Rational(int a = 0, int b = 1): real(a), imag(b)    // 1
    {
        cout << " Rational(int a = 0, int b = 0)" << endl;
    }
private:
    int real;
    int imag;
};
 
void func()
{
    Rational r;
    r = 100;  // 2
}
 
int main()
{
    func();
 
    return 0;
}
```

执行语句2时，由于Rational没有重载operator=(int i)，编译器会合成一个operator=(const Rational& another)函数，并执行逐位拷贝赋值操作，但由于100不是一个Rational对象，但编译器会尽可能查找合适的转换路径，以满足编译的需要。编译器发现存在一个Rational(int a = 0, int b = 1)构造函数，编译器会将语句2右侧的100通过Rational100, 1)生成一个临时对象，然后用编译器合成的operator=(const Rational& another)函数进行逐位赋值，语句2执行后，r对象内部的real为100，img为1。

C++编译器为了成功编译某些语句会生成很多从源码中不易察觉的辅助函数，甚至对象。C++编译器提供的自动类型转换确实提高了程序的可读性，简化了程序编写，提高了开发效率。但类型转换意味着临时对象的产生，对象的创建和销毁意味着性能的下降，类型转换还意味着编译器会生成其它的代码。因此，如果不需要编译器提供自动类型转换，可以使用explicit对类的构造函数进行声明。

```
#include <iostream>
using namespace std;
 
class Rational
{
public:
    explicit Rational(int a = 0, int b = 1): real(a), imag(b)    // 1
    {
        cout << " Rational(int a = 0, int b = 0)" << endl;
    }
private:
    int real;
    int imag;
};
 
void func()
{
    Rational r; // 2
    r = 100;    // 3
}
 
int main()
{
    func();
 
    return 0;
}
```

此时，进行代码编译会报错：

error: no match for ‘operator=’ (operand types are ‘Rational’ and ‘int’)
错误信息提示没有匹配的operator=函数将int和Rational对象进行转换。C++编译器默认合成的operator=函数只接受Rational对象，不能接受int类型作为参数。要想代码编译能够通过，方法一是提供一个重载的operator=赋值函数，可以接受整型作为参数；方法二是能够将整型转换为Rational对象，然后进一步利用编译器合成的赋值运算符。将整型转换为Rational对象，可以提供能只传递一个整型作为参数的Rational构造函数，考虑到缺省参数，调用构造函数可能会是无参、一个参数、两个参数，此时编译器可以利用整型变量作为参数调用Rational构造函数生成一个临时对象。由于explicit关键字限定了构造函数只能被显示调用，不允许编译器运用其进行类型转换，此时编译器不能使用构造函数将整型100转换为Rational对象，所以导致编译报错。

通过重载以整型作为参数的operator=函数可以成功编译，代码如下：

```
#include <iostream>
using namespace std;
 
class Rational
{
public:
    explicit Rational(int a = 0, int b = 1): real(a), imag(b)    // 1
    {
        cout << " Rational(int a = 0, int b = 0)" << endl;
    }
 
    Rational& operator=(int r)
    {
        real = r;
        imag = 1;
        return *this;
    }
 
private:
    int real;
    int imag;
};
 
void func()
{
    Rational r; // 2
    r = 100;    // 3
}
 
int main()
{
    func();
    return 0;
}
```

重载operator=函数后，编译器可以成功将整型数转换为Rational对象，同时成功避免了临时对象产生。

当一个函数返回的是非內建类型的对象时，返回结果对象必须在某个地方存放，编译器会从调用相应函数的栈帧中开辟空间，并用返回值作为参数调用返回值对象所属类型的拷贝构造函数在所开辟的空间生成对象，在调用函数结束并返回后可以继续利用临时对象。

```
#include <iostream>
#include <string>
 
using namespace std;
class Rational
{
public:
    Rational(int a = 0, int b = 0): real(a), imag(b)
    {
        cout << " Rational(int a = 0, int b = 0)" << endl;
    }
 
    Rational(const Rational& another): real(another.real), imag(another.imag)
    {
        cout << " Rational(const Rational& another)" << endl;
    }
 
    Rational& operator = (const Rational& other)
    {
        if(this != &other)
        {
            real = other.real;
            imag = other.imag;
        }
        cout << " Rational& operator = (const Rational& other)" << endl;
        return *this;
    }
    friend const Rational operator+(const Rational& a, const Rational& b);
private:
    int real;
    int imag;
};
 
const Rational operator+(const Rational& a, const Rational& b)
{
    cout << " operator+ begin" << endl;
    Rational c;
    c.real = a.real + b.real;
    c.imag = a.imag + b.imag;
    cout << " operator+ end" << endl;
    return c; // 2
}
 
int main()
{
    Rational r, a(10, 10), b(5, 8); 
    r = a + b;// 1
    return 0;
}
```

执行语句1时，相当于在main函数中调用operator+(const Rational& a, const Rational& b)函数，在main函数的栈中会开辟一块Rational大小的空间，在operator+(const Rational& a, const Rational& b)函数内部的语句2处，函数返回使用被销毁的c对象作为参数调用拷贝构造函数在main函数栈中开辟空间生成一个Rational对象。然后使用operator =执行赋值操作。编译如下：

```
g++ -fno-elide-constructors main.cpp
输出如下：

 Rational(int a = 0, int b = 0)
 Rational(int a = 0, int b = 0)
 Rational(int a = 0, int b = 0)
 operator+ begin
 Rational(int a = 0, int b = 0)
 operator+ end
 Rational(const Rational& another)
 Rational& operator = (const Rational& other)
 ```
由于r对象在默认构造后并没有使用，可以延迟生成，代码如下：

```
#include <iostream>
#include <string>
using namespace std;
 
class Rational
{
public:
    Rational(int a = 0, int b = 0): real(a), imag(b)
    {
        cout << " Rational(int a = 0, int b = 0)" << endl;
    }
 
    Rational(const Rational& another): real(another.real), imag(another.imag)
    {
        cout << " Rational(const Rational& another)" << endl;
    }
 
    Rational& operator = (const Rational& other)
    {
        if(this != &other)
        {
            real = other.real;
            imag = other.imag;
        }
        cout << " Rational& operator = (const Rational& other)" << endl;
        return *this;
    }
    friend const Rational operator+(const Rational& a, const Rational& b);
private:
    int real;
    int imag;
};
 
const Rational operator+(const Rational& a, const Rational& b)
{
    cout << " operator+ begin" << endl;
    Rational c;
    c.real = a.real + b.real;
    c.imag = a.imag + b.imag;
    cout << " operator+ end" << endl;
    return c; // 2
}
 
int main()
{
    Rational a(10, 10), b(5, 8);
    Rational r = a + b;  // 1
    return 0;
}
```

编译过程如下：

```
g++ -fno-elide-constructors main.cpp
输出如下： 

 Rational(int a = 0, int b = 0)
 Rational(int a = 0, int b = 0)
 operator+ begin
 Rational(int a = 0, int b = 0)
 operator+ end
 Rational(const Rational& another)
 Rational(const Rational& another)
 ```
分析代码，编译器执行语句1时语义发生了较大变化，编译器对=的解释不再是赋值操作符，而是对象r的初始化。在取得a+b的结果时，在main函数栈中开辟空间，使用c对象作为参数调用拷贝构造函数生成一个临时对象，然后使用临时对象作为参数调用拷贝构造函数生成r对象。

因此，对于非內建对象，尽量将对象延迟到确切直到其有效状态时，可以有效减少临时对象生成。如将Rational r；r = a + b;改写为Rational r = a + b;

进一步，可以将operator+函数改写为如下：

```
const Rational operator+(const Rational& a, const Rational& b)
{
    cout << " operator+ begin" << endl;
    return Rational(a.real + b.real, a.imag + b.imag); // 2
}
```

通常，operator+与operator+=需要以其实现，Rational的operator+=实现如下：

```
Rational operator+=(const Rational& a)
{
    real += a.real;
    imag = a.imag;
    return *this;
}
```
operator+=没有产生临时对象，尽量用operator+=代替operator+操作。考虑到代码复用性，operator+可以使用operator+=实现，代码如下：

```
const Rational operator+(const Rational& a, const Rational& b)
{
    cout << " operator+ begin" << endl;
    return Rational(a) += b; // 2
}
```

对于前自增操作符实现如下：

```
const Rational operator++()
{
    ++real;
    return *this;
}
```

对于后自增操作如下：

```
    const Rational operator++(int)
    {
        Rational temp(*this);
        ++(*this);
        return temp;
    }
```
      
前自增只需要将自身返回，后自增需要返回一个对象，因此需要多生成两个对象：函数体内的局部变量和临时对象，因此对于非內建类型，在保证程序语义下尽量使用前自增。

#### 3、临时对象的生命周期
C++规范中定义了临时对象的生命周期从创建时开始，到包含创建它的最长语句执行完毕。

```
string a, b;
const char* str;
if(strlen(str = (a + b).c_str()) > 5) // 1
{
    printf("%s\n", str);// 2
}
```
分析代码，语句1处首先创建一个临时对象存放a+b的值，然后将临时对象的内容通过c_str函数得到赋值给str，如果str长度大于5则执行语句2，但临时对象生命周期在包含其创建的最长语句已经结束，当进入if语句块时，临时对象已经被销毁，执行其内部字符串的str指向的是一段已经回收的内存，结果是无法预测的。但存在一个特例，当用一个临时对象来初始化一个常量引用时，临时对象的生命周期会持续到与绑定其上的常用引用销毁时。示例代码如下：

```
string a, b;
if(true)
{
    const string& c = a + b; // 1
}
```
语句1将a+b结果的临时对象绑定到常量引用c，临时对象生命周期会持续到c的作用域结束，不会在语句1结束时结束。

## 五、内联函数
#### 1、C++内联函数简介
C++语言的设计中，内联函数的引入完全是为了性能的考虑，因此在编写对性能要求较高的C++程序时，极有必要考量内联函数的使用。

内联是将被调用函数的函数体代码直接地整个插入到函数被调用处，而不是通过call语句进行。C++编译器在真正进行内联时，由于考虑到被内联函数的传入参数、自己的局部变量以及返回值的因素，不只进行简单的代码拷贝，还有许多细致工作。

#### 2、C++函数内联的声明
开发人员可以有两种方法告诉C++编译器需要内联哪些类成员函数，一种是在类的定义体外，一种是在类的定义体内。

###### （1）在类的定义体外时，需要在类成员函数的定义前加inline关键字，显式地告诉C++编译器本函数在调用时需要内联处理。

```
class Student
{
public:
    void setName(const QString& name);
    QString getName()const;
    void setAge(const int age);
    int getAge()const;
private:
    QString m_name;
    int m_age;
};
 
inline void Student::setName(const QString& name)
{
    m_name = name;
}
 
inline QString Student::getName()const
{
    return m_name;
}
 
inline void Student::setAge(const int age)
{
    m_age = age;
}
 
inline int Student::getAge()const
{
    return m_age;
}
```

###### （2）在类的定义体内且声明成员函数时，同时提供类成员函数的实现体。此时，inline关键字不是必须的。

```
class Student
{
public:
    void setName(const QString& name)
    {
        m_name = name;
    }
 
    inline QString getName()const
    {
        return m_name;
    }
 
    inline void setAge(const int age)
    {
        m_age = age;
    }
 
    int getAge()const
    {
        return m_age;
    }
private:
    QString m_name;
    int m_age;
};
```

###### （3）普通函数（非类成员函数）需要被内联时，需要在普通函数的定义前加inline关键字，显式地告诉C++编译器本函数在调用时需要内联处理。

```
inline int add(int a, int b)
{
    return a + b;
}
```

### 3、C++内联机制
C++是以编译单元为单位编译的，通常一个编译单元基本等同于一个CPP文件。在编译的预处理阶段，预处理器会将#include的各个头文件（支持递归头文件展开）完整地复制到CPP文件的对应位置处，并进行宏展开等操作。预处理器处理后，编译才真正开始。一旦C++编译器开始编译，C++编译器将不会意识到其它CPP文件的存在，因此并不会参考其它CPP文件的内容信息。因此，在编译某个编译单元时，如果本编译单元会调用到某个内联函数，那么内联函数的函数定义（函数体）必须包含在编译单元内。因为C++编译器在使用内联函数体代码替换内联函数调用时，必须知道内联函数的函数体代码，并且不能通过参考其它编译单元信息获得。

如果多个编译单元会用到同一个内联函数，C++规范要求在多个编译单元中同一个内联函数的定义必须是完全一致的，即ODR（One Definition Rule）原则。考虑到代码的可维护性，通常将内联函数的定义放在一个头文件中，用到内联函数的所有编译单元只需要#include相应的头文件即可。

```
#include <iostream>
#include <string>
 
using namespace std;
class Student
{
public:
    void setName(const string& name)
    {
        m_name = name;
    }
 
    inline string getName()const
    {
        return m_name;
    }
 
    inline void setAge(const int age)
    {
        m_age = age;
    }
 
    inline int getAge()const
    {
        return m_age;
    }
 
private:
    string m_name;
    int m_age;
};
 
void Print()
{
    Student s;
    s.setAge(20);
    cout << s.getAge() << endl;
}
 
int main()
{
    Print();
    return 0;
}
```

上述代码中，在不开启内联时调用函数Print的函数时相关的操作如下：

```
（1）进入Print函数时，从其栈帧中开辟了放置s对象的空间。

（2）进入函数体后，首先在开辟的s对象存储空间执行Student的默认构造函数构造s对象。

（3）将常数20压栈，调用s的setAge函数（开辟setAge函数的栈帧，返回时回退销毁此栈帧）.

（4）执行s的getAge函数，并将返回值压栈.

（5）调用cout操作符操作压栈的结果，即输出。
```

开启内联后，Print函数的等效代码如下：

```
void Print()
{
    Student s;
    {
        s.m_age = 20;
    }
    int tmp = s.m_age;
    cout << tmp << endl;
}
```
函数调用时的参数压栈，栈帧开辟与销毁等操作不再需要，结合内联后代码，编译器会进一步优化为如下结果：

```
int main()
{
    cout << 20 << endl;
    return 0;
}
```
如果不考虑setAge/getAge函数内联，对于非内联函数一般不会在头文件中定义，因此setAge/getAge函数可能在本编译单元之外的其它编译单元定义，Print函数所在的编译单元会看不到setAge/getAge，不知道函数体的具体代码信息，不能作出进一步的代码优化。

因此，函数内联的优点如下：
```
A、减少因为函数调用引起的开销，主要是参数压栈、栈帧开辟与回收、寄存器保存与恢复。

B、内联后编译器在处理调用内联函数的函数时，因为可供分析的代码更多，因此编译器能做的优化更深入彻底。
```
程序的唯一入口main函数肯定不会被内联化，编译器合成的默认构造函数、拷贝构造函数、析构函数以及赋值运算符一般都会被内联化。编译器并不保证使用inline修饰的函数在编译时真正被内联处理，inline只是给编译器的建议，编译其完全会根据实际情况对其忽视。

### 4、函数调用机制
```
int add(int a, int b)
{
    return a + b;
}
 
void func()
{
    ...
    int c = add(a, b);
    ...
}
```
函数调用时相关操作如下：

```
（1）参数压栈

参数是a，b；压栈时通常按照逆序压栈，因此是b，a；如果参数中有对象，需要先进行拷贝构造。

（2）保存返回地址

即函数调用结束后接着执行的语句的地址。

（3）保存维护add函数栈帧信息的寄存器内容，如SP（对栈指针），FP（栈栈指针）等。具体保存的寄存器与硬件平台有关。

（4）保存某些通用寄存器的内容。由于某些通用寄存器会被所有函数用到，所以在func函数调用add之前，这些通用寄存器可能已经存储了对func有用的信息。但这些通用寄存器在进入add函数体内执行时可能会被add函数用到，从而被覆写。因此，func函数会在调用add函数前保存一份这些通用寄存器的内容，在add函数返回后恢复。

（5）调用add函数。首先通过移动栈指针来分配所有在其内部声明的局部变量所需的空间，然后执行其函数体内的代码。

（6）add函数执行完毕，函数返回时，func函数需要进行善后处理，如恢复通用寄存器的值，恢复保存func函数栈帧信息的寄存器的值，通过移动栈指针销毁add函数的栈帧，将保存的返回地址出栈并赋值给IP寄存器，通过移动栈指针回收传给add函数的参数所占的空间。
```

如果函数的传入参数和返回值都为对象时，会涉及对象的构造与析构，函数调用的开销会更大。

### 5、内联的效率分析
因为函数调用的准备与善后工作最终都由机器指令完成，假设一个函数之前的准备工作与之后的善后工作的指令所需的空间为SS，执行指令所需的时间为TS，从时间和空间分析内联的效率如下：

```
（1）空间效率。通常认为，如果不采用内联，被调用函数代码只有一份，在调用位置使用call语句即可。而采用内联后，被调用函数的代码在所调用的位置都会有一份拷贝，因此会导致代码膨胀。
```

如果函数func的函数体代码为FuncS，假设func函数在整个程序内被调用n次，不采用内联时，对func函数的调用只有准备工作与善后工作会增加最后的代码量开销，func函数相关的代码大小为n*SS + FuncS。采用内联后，在各个函数调用位置都需要将函数体代码展开，即func函数的相关代码大小为n*FuncS。所以需要比较

n*SS + FuncS与n*FuncS的大小，如果调用次数n较大，可以简化为比较SS与FuncS的大小。如果内联函数自己的函数体代码量比因为函数调用的准备与善后工作引入的代码量大，则内联后程序的代码量会变大；如果内联函数自己的函数体代码量比因为函数调用的准备与善后工作引入的代码量小，则内联后程序的代码量会变小；如果内联后编译器因为获得更多的代码信息，从而对调用函数的优化更深入彻底，则最终的代码量会更小。

```
（2）时间效率。通常，内联后函数调用都不再需要做函数调用的准备与善后工作，并且由于编译器可以获得更多的代码信息，可以进行深入彻底的代码优化。内联后，调用函体内需要执行的代码是相邻的，其执行的代码都在同一个页面或连续的页面中。如果没有内联，执行到被调用函数时，需要调转到包含被调用函数的内存页面中执行，而被调用函数的所属的页面极有可能当时不在物理内存中。因此，内联后可以降低缺页的概率，减少缺页次数的效果远比减少一些代码量执行的效果要好。即使被调用函数所在页面也在内存中，但与调用函数在空间上相隔甚远，可能会引起cache miss，从而降低执行速度。因此，内联后程序的执行时间会比没有内联要少，即程序执行速度会更快。但如果FunS远大于SS，且n较大，最终程序的大小会比没有内联大的多，用来存放代码的内存页也会更多，导致执行代码引起的缺页也会增多，此时，最终程序的执行时间可能会因为大量的缺页变得更多，即程序变慢。因此，很多编译器会对函数体代码很多的函数拒绝其内联请求，即忽略inine关键字，按照非内联函数进行编译。
```

因此，是否采用内联时需要根据内联函数的特征（如函数体代码量、程序被调用次数等）进行判断。判断内联效果的最终和最有效方法还是对程序执行速度和程序大小进行测量，然后根据测量结果决定是否采用内联和对哪些函数进行内联。

### 6、内联函数的二进制兼容问题
调用内联函数的编译单元必须具有内联函数的函数体代码信息，考虑到ODR规则和代码可维护性，通常将内联函数的定义放在头文件中，每个调用内联函数的编译单元通过#include相应头文件。

在大型软件中，某个内联函数因为比较通用，可能会被大多数编译单元用到，如果对内联函数进行修改会引起所有用到该内联函数的编译单元进行重新编译。对于大型程序，重新编译大部分编译单元会消耗大量的编译时间，因此，内联函数最好在开发的后期引入，以避免可能不必要的大量编译时间浪费。

如果某开发组使用了第三方提供的程序库，而第三方程序库中可能包含内联函数，因此在开发组代码中使用了第三方库的内联函数位置都会将内联函数体代码拷贝到函数调用位置。如果第三方库提供商在下一个版本中修改了某些内联函数的定义，即使没有修改任何函数的对外接口，开发组想要使用新版本的第三方库仍然需要重新编译。如果程序已经发布，则重新编译的成本会极高。如果没有内联，第三方库提供商只是修改了函数实现，开发组不必重新编译即可使用最新的第三方库版本。

### 7、递归函数的内联
内联的本质是使用函数体代码对函数调用进行替换，对于递归函数：

```
int sum(int n)
{
    if(n < 2)
    {
        return 1;
    }
    else
    {
        return sum(n - 1) + n;
    }
}
```
如果某个编译单元内调用了sum函数，如下：

```
void func()
{
    ...
    int ret = sum(n);
    ...
}
```
如果在编译本编译单元且调用sum函数时，提供的参数n不能够知道实际值，则编译器无法知道对sum函数进行了多少次替换，编译器会拒绝对递归函数sum进行内联；如果在编译本编译单元且调用sum函数时，提供的参数n可以知道实际值，则编译器可能会根据n的大小来判断时都对sum函数进行内联，如果n很大，内联展开可能会使最终程序的大小变得很大。

### 8、虚函数的内联
内联函数是编译阶段的行为，虚函数是执行阶段行为，因此编译器一般会拒绝对虚函数进行内联的请求。虚函数不能被内联是由于编译器在编译时无法知道调用的虚函数到底是哪一个版本，即无法确定虚函数的函数体，但在两种情况下，编译器能够知道虚函数调用的真实版本，因此可以内联。

一是通过对象而不是指向对象的指针或引用对虚函数进行调用，此时编译器在编译器已经知道对象的确切类型，因此会直接调用确切类型的虚函数的实现版本，而不会产生动态绑定行为的代码。

二是虽然通过对象指针或对象引用调用虚函数，但编译器在编译时能够知道指针或引用指向对象的确切类型，如在产生新对象时做的指针赋值或引用初始化与通过指针或引用调用虚函数处于同一编译单元，并且指针没有被改变赋值使其指向到其它不能知道确切类型的对象，此时编译器也不会产生动态绑定的代码，而是直接调用确切类型的虚函数实现版本。

```
inline virtual int x::y(char* a)
{
    ...
}
 
void func(char* b)
{
    x_base* px = new x();
    x ox;
    px->y(b);
    ox.y(b);
}
```
### 9、C++内联与C语言宏的区别
C语言宏与C++内联的区别如下：

```
（1）C++内联是编译阶段行为，宏是预处理行为，宏的替代展开由预处理器负责，宏对于编译器是不可见的。

（2）预处理器不能对宏的参数进行类型检查，编译器会对内联函数的参数进行类型检查。

（3）宏的参数在宏体内出现两次以上时通常会产生副作用，尤其是当在宏体内对参数进行自增、自减操作时，内联不会。

（4）宏肯定会被展开，inline修饰的函数不一定会被内联展开。
```


————————————————
版权声明：本文为CSDN博主「天山老妖」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/A642960662/article/details/123029265
