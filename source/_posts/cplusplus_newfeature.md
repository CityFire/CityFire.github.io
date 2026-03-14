---
title: C++11新特性
tags: [C++]
categories: [C++]
---

本文列举一下C++11相比C++98的一些重要变化，做一下知识总结和沉淀。
## 1. 指针空值（0，NULL，nullptr）
在以前，初始化指针的时候一般将其设置NULL(或者0)，NULL是一个宏定义，在传统C头文件stddef.h中定义
```
#undef NULL
#if defined(__cplusplus)
#define NULL 0
#else
#define NULL ((void*)0)
#endif
```
NULL因其字面常量0的二义性，在某些场景（例如，函数重载）的使用会遇到麻烦，C++11 引入关键字nullptr来避免二义性，nullptr是一个”指针空值常量”，仅可以被隐式转换为指针类型。
```
#include <stdio.h>

void f(char* c)
{
    printf("invoke f(char*)\n");
}

void f(int i)
{
    printf("invoke f(int)\n");
}

int main()
{
    f(0);// 可以编译过，调用void f(int i)。
    f(NULL);// 编译不过，报：error: call to 'f' is ambiguous。
    f(nullptr);// 可以编译通过，调用void f(char* c)。
    f((char*) 0);// 可以编译过,调用void f(char* c)。
    int n1 = nullptr; // 编译不过，报error: cannot initialize a variable of type 'int' with an rvalue of type 'nullptr_t'。
    int n2 = (int)nullptr; // 编译不过，即使强转也不行，报error: cast from pointer to smaller type 'int' loses information。
    int n3 = reinterpret_cast<int>(nullptr);// 编译不过，即使强制也不行，报error: cast from pointer to smaller type 'int' loses information
}
```

## 2. nullptr 与nullptr_t
nullptr 是一个指针空值常量， nullptr_t是一个指针空值类型，一个是常量，一个是类型。既然nullptr_t是一个类型，则说明两件事情：1）指针空值并非仅有nullptr一个，可以通过nullptr_t来声明一个指针空值类型的变量（用途不大）。2）nullptr_t是一个类型，不能直接使用，需要先声明一个实例。
nullptr 是一个关键字，不需要包含任何头文件，使用nullptr_t的时候需 包含cstddef。
```
#include <stdio.h>
#include <cstddef>

int main()
{
    std::nullptr_t myNullPtr;
    if(myNullPtr == nullptr)
    {
        printf("test std::nullptr_t\n");
    }
}
```

## 3. = default
在C++中声明自定义的类，编译器会默认帮助程序员生成一些他们未显示定义的成员函数，包括构造函数、拷贝构造函数、拷贝赋值函数（operator =）、移动构造函数、移动拷贝函数、析构函数。一旦程序员实现了这些函数的自定义版本，则编译器不会再为该类自动生成默认版本。例如，声明了带参数的构造函数版本，则必须声明不带参数的版本以完成无参的变量初始化，而这会导致对应的类不再是POD的（非POD类型，意味着编译器失去了优化这样简单的数据类型的可能），通过=default 可以使其重新成为POD类型，见如下几个例子。
```
#include <type_traits>
#include <iostream>

class A{
    private:
        int data;
};

class B{
    public:
        B(int i)
            :data(i)
        {}
    private:
        int data;
};

class C{
    public:
        C()
        {}

        C(int i)
            :data(i)
        {}
    private:
        int data;
};

class D{
    public:
        D() = default;

        D(int i)
            :data(i)
        {}
    private:
        int data;
};

int main()
{
    std::cout << std::is_pod<A>::value << std::endl;// 打印1
    std::cout << std::is_pod<B>::value << std::endl;// 打印0
    std::cout << std::is_pod<C>::value << std::endl;// 打印0
    std::cout << std::is_pod<D>::value << std::endl;// 打印1
}
```

## 4. = delete
在以前，程序员若希望限制一些默认函数的生成，例如，单件类的实现需要阻止其生成拷贝构造函数和拷贝赋值函数，可以将拷贝构造函数和拷贝赋值函数声明为private成员，并且不提供函数实现，C++11 标准给出了非常简洁的方法，即在函数的定义或者声明加上”= delete“。
```
#include <iostream>

class NoCopyConstructor
{
    public:
        NoCopyConstructor() = default;

        NoCopyConstructor(int i)
            :data(i)
        {
        }
    private:
        NoCopyConstructor(const NoCopyConstructor&);
    private:
        int data;
};

class NoCopyConstructor2
{
    public:
        NoCopyConstructor2() = default;

        NoCopyConstructor2(int i)
            :data(i)
        {
        }
        NoCopyConstructor2(const NoCopyConstructor2&) = delete;

    private:
        int data;
};

int main()
{
    NoCopyConstructor a;
    NoCopyConstructor b(a);// 编译不过，报error: calling a private constructor of class 'NoCopyConstructor'
    
    NoCopyConstructor2 a2;
    NoCopyConstructor2 b2(a2);// 编译不过， 报error: call to deleted constructor of 'NoCopyConstructor2'
}
```

## 5. 左值，右值（右值又分将亡值、纯右值）
将亡值是C++11新增的跟右值引用相关的表达式，通常是要被移动的对象。右值引用，对右值进行引用的类型，因为右值通常没有名字，所以只能用引用的方式找到他的存在，举例，T&& a = ReturnRvalue(); ReturnRvalue()必须返回一个右值，不能返回左值。右值引用和移动语义紧密联系，可以延续右值的生命周期，并且可以对右值进行修改； 虽然可以定义常量右值引用，但是意义不大。
一般来说，左值引用不能接受一个右值，不过常量的左值引用是能接受一个右值的，比如，函数的引用传递，const T&, 可以减少临时对象的拷贝。
is_rvalue_reference, is_lvalue_reference, is_reference 可以判断是左值引用、右值引用、引用。举例，is_revalue_reference<string &&>::value ， value取值true。
std::move , 可以强制将一个左值转化为右值，以便可以通过右值引用使用该值，从而实现移动语义。对堆内存、文件句柄等资源成员使用move，如果成员支持移动构造，则可以实现移动语义，若成员没有移动构造函数，参数类型为常量左值引用的构造函数版本也会轻松的实现拷贝构造；
```
#include <iostream>
#include <utility>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string str = "Hello World!";
    vector<string> v;

    // 使用 push_back(const T&) ， 复制str的内容，不是移动
    v.push_back(str);
    // 打印如下:After copy, str is "Hello World!"
    cout << "After copy, str is \"" << str << "\"\n";

    // 使用右值引用 push_back(T&&) ，移动str的内容，不是复制，
    v.push_back(move(str));
    // 打印如下:After move, str is ""
    cout << "After move, str is \"" << str << "\"\n";

    // 打印如下(包含第一次复制进来的，总共两个):The contents of the vector are "Hello World!", "Hello World!"
    cout << "The contents of the vector are \"" << v[0] << "\", \"" << v[1] << "\"\n";
}
```

## 6. 列表初始化，C++11新增了列表初始化方式，方便了代码编写。声明一个以initializer_list<T> 模板类为参数的构造函数，自定义的类可以使用列表初始化方式。

```
int b[]{2,4,5};			
vector<int> c{1,3,5};			
map<int, float> d = { {1,1.0f}, {2, 2.0f}, {5, 3.2f} };			
int a = {3+4};			
int a{3+4};			
int a(3+4);

vector<T>::vector<T>(initializer_list<T>  elements)
{
......
}
std::vector<int> vec= {1,2,3,4,5};

```

## 7. 扩展了using的使用，不只用来声明命名空间了，using namespace xxx;
```
     using uint = unsigned int ;
			
     template<typename T> 
     using MapString = map<T, char*>;			
     MapString<int> numberedString;			
```

## 8. auto
C++98中用于自动存储期的局部变量，此特性几乎无人使用；C++11改变了语义，作为新的类型指示符，用于自动推导，特别是命名空间、模板等导致类型很长的时候，非常方便。对于指针类型，声明为auto* 或者auto 是一样的，对于引用类型，必须使用auto & 。
```
int x;			
int * y = &x;			
double foo(){			
    return 2.0;			
}			
auto*a = &x;			
auto c = y;			
auto * d = y;			
//auto * e = &foo();---这个有问题，指针不能指向临时变量			
			
auto & b = x;			
const auto &f = foo();			
auto &&f = foo();			
			
auto g = x;	                                                                                   		
auto & h = x;	
```

## 9. decltype,以一个普通的表达式为参数返回该表达式的类型，在编译期进行。
```
template <typename T1, typename T2>
auto Mul(const T1& t1, const T2& t2) -> decltype(t1 * t2){
    return t1 * t2;
}
```
   			
## 10. 基于范围的for循环，对于知道范围的数组和stl容器，C++11提供了for迭代访问能力，结合auto，可简化代码。需要满足两个条件：1)迭代的对象实现++和==操作；2)知道范围
```
int main() {		
    vector<int> v = {1,2,3,4,5};		
    for(auto i = v.begin(); i != v.end();++i)		
    {		
        cout << *i << '\t';		
    }		
    cout << endl;		
		
    for(auto &e:v){		
        e *= 2;		
    }		
		
    for(auto e:v)		
    {		
        cout << e << '\t';		
    }		
    cout << endl;		
}	
```

## 11. 多线程编程
C++11之前，在C/C++中程序中使用线程，主要使用POSIX线程（pthread），POSIX线程是POSIX标准中关于线程的部分，程序员可以通过pthread线程的api完成线程的创建、数据的共享、同步等功能。C++11引入了多线程的支持，使得C/C++语言在进行线程编程时，不必依赖第三方库和标准。
```
C++98 实现的多线程
#include <pthread.h>			
#include <iostream>			
using namespace std;			
static long long total = 0;			
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;			
			
void* func(void*){			
    long long i;			
    for(i = 0; i < 100000000L;++i){			
        pthread_mutex_lock(&m);			
        total += i;			
        pthread_mutex_unlock(&m);			
    }			
    return NULL;			
}			
			
int main(){			
    pthread_t thread1, thread2;			
    if(pthread_create(&thread1, NULL, &func, NULL)){			
        throw;			
    }			
    if(pthread_create(&thread2, NULL, &func, NULL)){			
        throw;			
    }			
			
    pthread_join(thread1, NULL);			
    pthread_join(thread2, NULL);			
			
    cout << total << endl;			
    return 0;			
}
```
```			
C++11 实现的多线程
#include <atomic>		
#include <thread>		
#include <iostream>		
		
using namespace std;		
		
atomic_llong total{0};		
		
void func(int ){		
    for (long long i = 0; i < 100000000LL;++i){		
        total += i;		
    }		
}		
		
int main(){		
    thread t1(func, 0);		
    thread t2(func ,0);		
    t1.join();		
    t2.join();		
    cout << total << endl;		
    return 0;		
}	
```

## 12. 智能指针
C++98中，智能指针采用auto_ptr ,拷贝的时候返回的是一个左值，且不能调用delete[], C++11 已经废弃,改用如下三种智能指针：

`unique_ptr`：拥有管理内存的所有权，没有拷贝构造函数，只有移动构造函数，不能多个unique_ptr对象共享一段内存，可以自定义delete函数，从而支持delete [] 。

`share_ptr`：通过计数方式多个share_ptr可以共享一段内存，当计数为0的时候，所管理内存会被删除，可以自定义delete函数，从而支持delete[] 。

`weak_ptr`：观察shared_ptr管理的内存对象 ，只观察但不拥有。成员函数lock返回shared_ptr对象，若对应内存已经删除，则shared_ptr对象==nullptr，weak_ptr对象可以拷贝构造，拷贝构造出来的对象和原对象观察的是同一段内存。成员函数reset可以解除对内存的观察，注意，是解除观察，并不会删除对应内存对象。可以避免因shared_ptr的循环引用而引起的内存泄露，见如下对比使用方式：
```
#include <memory>
#include <string>
#include <iostream>

using namespace std;

class B;
class A
{
    public:
        shared_ptr<class B> m_spB;
};


class B
{
    public:
        shared_ptr<class A> m_spA;
};

class D;
class C
{
    public:
        weak_ptr<class D> m_wpD;
};


class D
{
    public:
        weak_ptr<class C> m_wpC;
};


void test_loop_ref()
{
    weak_ptr<class A> wp1;

    {
        auto pA = make_shared<class A>();
        auto pB = make_shared<class B>();

        pA->m_spB = pB;
        pB->m_spA = pA;

        wp1 = pA;
    }

    cout << "wp1 reference number: " << wp1.use_count() << "\n";// 存在内存泄露，打印如下，wp1 reference number:1

    weak_ptr<class C> wp2;
    {
        auto pC = make_shared<class C>();
        auto pD = make_shared<class D>();

        pC->m_wpD = pD;
        pD->m_wpC = pC;

        wp2 = pC;
    }

    cout << "wp2 reference number: " << wp2.use_count() << "\n";// 没有内存泄露，打印如下，wp2 reference number:0
}

int main()
{
    //std::weak_ptr 用来避免 std::shared_ptr 的循环引用
    test_loop_ref();

    return 0;
}
```

## 13. lambda
lambda被用来表示一种匿名函数，这种匿名函数代表了一种所谓的lambda calculus。以lambda概念为基础的”函数式编程“是与命令式编程、面向对象编程等并列的一种编程范型。
```
[capture](parameters)mutable ->return-type{statement}
```
其中，
[capture] :捕捉列表，[]是lambda引出符，编译器根据该引出符判断接下来的代码是否是lambda函数。捕捉列表用于捕捉父域中的变量以供lambda函数使用，[var]表示以值传递方式捕捉父域中的变量var，[=]表示以值传递方式捕捉父域中的所有变量（包括this），[&var]表示以引用传递方式捕捉父域中的变量var，[&]表示以引用传递方式捕捉父域中的所有变量（包括this）,[this]表示以值传递方式捕捉当前的this指针。

(parameters):参数列表，与普通函数的参数列表一致，如果不需要参数传递，则可以连同括号()一起省略。

mutable: mutable修饰符，默认情况下，lambda函数总是一个const函数，mutable可以取消其常量性。在使用该修饰符时，参数列表不可省略（即使参数为空）。

->return-type: 返回类型，用追踪返回类型形式声明函数的返回类型，不需要返回值的时候可以连同符号->一起省略。在返回类型明确的情况下，也可以省略该部分，让编译器对返回类型进行推导。

{statement}: 函数体，内容与普通函数一样，不过除了可以使用参数之外，还可以使用所有捕获的变量。
```
#include <iostream>

int main()
{
    int a = 3;
    int b = 4;
    int c = 5;
    auto fun = [=, &b](int c) ->int {
        return b += a + c;
    };
   std::cout << "fun ret=" << fun(c) << std::endl;// 打印12
   std::cout << "b =" << b << std::endl;// 打印12
}
```

### ①函数对象参数
[]，标识一个launbda 的开始，这部分必须存在，不能省略。函数对象参数是传递给编译器自动生成的函数对象类的构造函数的。函数对象参数只能使用那些到定义 lambda
为止时 lambda 所在作用范围内可见的局部变量（包括 lambda 所在类的this)。

函数对象参数有以下形式：
```
空。没有使用任何函数对象参数。
=。函数体内可以使用lamabda 所在作用范国内所有可见的局部变量 （包括 lambde
所在类的this），并且是值传递方式(相当于编译器自动为我们技值传递了所有局部变量）

＆。函数体内可以使用 lambda 所在作用范国内所有可见的局部变量（包括 lambda所在类的 this），并且是引用传递方式(相当于编译器自动为我们按引用传递了所有局部变量）
this。 函数体内可以使用 lamnbda 所在类中的成员变量。

a。将a按值进行传递。按值进行传递时，函数体内不能修改传递进来的a的拷贝，
因为默认情况下函数是const 的。要修改传递进来的a的拷贝，可以添加 mutable修饰符。
＆a。将a按引用进行传递。

a&b。将a按值进行传递，b按引用进行传递。

=，&a,&b。除a和6按引用进行传递外，其他参数都按值进行传递。

＆,a,b。除a和b按值进行传递外，其他参数都按引用进行传递。
```

## 14. C++11 新增_Pragma("once")来保证头文件只会被include一次，用以代替先前的两种写法,_Pragma是一个操作符，可以用在宏定义中，比预处理指令灵活。
```
1)#pragma once 
2)#ifndef THIS_HEADER
  #define THIS_HEADER
  #endif
```

## 15. 变长参数的宏定义是指在宏定义中参数列表的最后一个参数为省略号，预定义宏__VA_ARGS__可以在宏定义的实现部分替换省略号所代表的字符串。
```
#define PR(...) printf(__VA_ARGS__)
```

## 16. 在C++98中，将char转换成wchar_t是未定义行为，到了C++11中，将char和wchart进行连接时，会先将char转成wchar_t，然后再与宽字符进行连接。

## 17. long long 有两种类型，long long 和unsigned long long ，不同平台可以有不同长度，至少是64位。

## 18. 经常会发现UINT、_int16、u64、int64_t,这些类型有的是源自编译器的自行扩展，有的则是来自某些编程环境（比如工作在Linux内核），C++标准中只定义了5种标准的有符号类型，同时规定每一种有符号整型都有一种对应的无符号整型版本，且两者具有相同的存储空间，signed char、signed short int、signed int、signed long int、signed long long int。

## 19. C、C++混用头文件的典型做法如下，可以让如下头文件被#include到C文件中，也可以被#include 到C++文件中, extern "C"可以抑制C++对函数名、变量名等符号进行名称重整，因此编译出的C目标文件和C++目标文件中的变量名和函数名都一样的。
```
#ifdef __cplusplus
extern "C"{
#endif

.....

#ifdef __cplusplus
"}"
#endif
```
__cplusplus通常被定义为一个整数值，C++03标准中，其值是199711L， 在C++11中是201103L, 可以据此写出只支持C++11的代码，以下代码插入那些只能用C++11编译器编译的代码中（因为代码含C++11特性）
```
#if __cplusplus < 201103L
#error "should use c++ 11 implementation"
#endif
```

## 20. C++11新增了静态断言static_assert, 即在预处理阶段做一些断言，静态断言的表达式结果必须是在编译期可以计算的表达式，可以放在任何名字空间，包括函数外部。assert只能用于运行时，且只能放在函数内部。

## 21. 用操作符noexcept替代原先的throw
如下用法已经被c++废弃:
```
void excpt_func() throw (int , doulbe){}  
void excpt_func() throw(){}
```
改为如下方式，可以没有常量表达式，默认是true:
```
void excpt_func() noexcept(常量表达式)
```

## 22. 快速初始化成员变量
非常量的静态成员变量，C++98 和C++11 保持一致，都需要到类的头文件以外去定义，保证编译时非常量的类静态成员的定义最后只存在于一个目标文件中。

非静态的成员变量，C++98只能在初始化列表中进行初始化，C++ 11增加支持就地初始化（用{}方式，不能用()方式），若同时对一个非静态的成员变量进行就地初始化和初始化列表初始化，最后起作用的是初始化列表（即后起作用）。

常量的静态成员变量，C++98和C++11都支持就地初始化，C++98只支持整型或者枚举类型

## 23. C++98, sizeof 只能对实例的变量或者类的静态成员进行操作，不能对类的非静态成员进行操作，若要想达成对类的非静态成员的操作，可以用如下ugly方式, 0强转成对象的指针，并解析访问对应非静态成员变量。C++11之后，可以对类的非静态成员进行操作，无需此ugly方式。
```
#include <iostream>		
		
using namespace std;		
		
struct People{		
    public:		
        int hand;		
        static People* all;		
};		
		
int main(){		
    People p;		
    cout << sizeof(p.hand) << endl;		
		
    cout << sizeof(People::all) << endl;		
		
    cout << sizeof(((People*)(0))->hand) <<endl;		
}		
```

## 24. friend, C++98 需要friend class XX，即需要关键字class，C++11只需要friend XX，不再要求有关键字class，因这一点改动，可以为类模板声明友元了（以前不行）。如果是基本类型，friend int不会生成。

## 25. final，给程序员一种中途终止派生的能力，控制力更强。如果一开始就不想派生，最开始的基类设置为非虚函数就可以了，final一般用于中途终止派生。override, 明确告知这个函数是继承、重载的，避免以前写法的混淆。这两个关键字用于函数后面，才会产生此效果。虽然变量名可以用这两个，但是不建议。

## 26. C++98支持类模板的默认模板参数，不支持函数模板的默认模板参数，C++11可以支持函数模板的默认模板参数。类模板的默认模板参数需要从右到左依次，函数模板的默认模板参数没有此约束。默认模板参数通常是需要跟默认函数参数一起使用的。

## 27. 外部模板，extern 显示实例化一个模板函数（类），可以避免在多个编译单元都重复生成模板函数（类）的实例化代码，虽然在链接的时候会判断代码相同而做合并，但是会增加开销，有了外部模板，则可以大大缓解此问题。

## 28. 局部的类型、匿名的类型在C++98中不能作为模板类的实参，C++11已放开此限制。不过，匿名类型不能直接写在模板类的参数类型中，必须用独立的表达式语句。

## 29. 继承构造函数
通过using声明基类构造函数，不需要像C++98那样，针对每个基类的构造函数，重新写一一遍（调用基类的构造函数）。这种做法，在C++98里面只针对普通成员函数，C++11将其扩展到构造函数了。

## 30. 委派构造函数
C++11中，一个构造函数可以委派其他构造函数完成对象的构造，C++98中，需要将公共逻辑提取成一个公共私有函数，然后被多个构造函数调用。

委派构造函数:调用目标构造函数完成构造的构造函数;

目标构造函数:基准的构造函数，被委派构造函数调用。构造函数不能既是委派构造函数，又含有初始化列表。

目标构造函数抛出异常，委派构造函数可以catch住（委派构造函数的函数体不会再执行），但是最终程序还是会core dump的，见如下小程序演示：
```
class DCExcept{			
    public:			
        DCExcept(double d)			
            try : DCExcept(1, d){			
                cout << "run the body." << endl;			
            }catch(...){			
                cout << "caught exception."<<endl;			
            }			
    private:			
        DCExcept(int i, double d){			
            cout << "going to throw" << endl;			
            throw 0;			
        }			
			
        int type;			
        double date;			
};			
going to throw			
caught exception.			
libc++abi.dylib: terminating with uncaught exception of type int			
Abort trap: 6	
```

## 31. 非受限联合体
C++98标准：不允许非POD类型，不允许拥有静态或者引用类型的成员。

C++11标准：任何非引用类型都可以成为联合体的数据成员。

C++11 匿名非受限联合体可以用于类的声明中，这给存在大量字段（不同场景，部分字段使用）放在一起提供了便利。

## 32. 字面量操作符函数
下面函数会解析以_C为后缀（后缀可以自己定义）的字符串，并返回一个T的临时变量, 括号中参数列表取决于实际情况会有不同，operator "" 与用户自定义后缀之间必须有空格，后缀建议以下划线开始，否则会编译器告警。
```
T operator "" _C (const char* col, size_t n)
```
若字面量为整型数，字面量操作符函数只可接受unsigned long long 或者 const char* 为其参数， 当unsigned long long 无法容纳该字面量的时候，编译器会自动将字面量转换为以\0为结尾符的字符串，并调用const char* 为参数的版本进行处理。

若字面量为浮点类型，则字面量操作符函数只可接受long double 或者const char* 为参数，const char*版本的使用规则同第一点（过长则使用const char*版本）。

若字面量为字符串，则字面量操作符函数只可接受const char* ,size_t为参数（已知长度的字符串）。

若字面量为字符，则字面量操作函数只可接受一个char为参数。
```
long double operator "" _w(long double);
std::string operator "" _w(const char16_t*, size_t);
unsigned operator "" _w(const char*);
int main() {
    1.2_w; // 调用运算符 "" _w(1.2L)
    u"one"_w; // 调用运算符 "" _w(u"one", 3)
    12_w; // 调用运算符 "" _w("12")
    "two"_w; // 错误：无适用的字面量运算符
}
```

## 33. 枚举类型
针对C++98中枚举类型的一些缺点，C++11做了如下扩展：

在C++98中，枚举值没有类或者命名空间的约束，两个枚举类型的枚举值若是一样，则会产生冲突， 在C++11中，采用类名来约束，从而避免了冲突。

在C++98中，枚举值和整型可以隐式转换，在C++11中，必须显示转换。

在C++98中，底层存储大小不确定，在C++11中，可以指定底层存储类型。

// C++11中的用法  
```
enum Type:char{General,Light, Medium, Heavy};			
enum class Type:char{General, Light, Medium, Heavy};	
```

## 34. 最小垃圾回收支持
安全派生指针定义：

在解引用基础上的引用，例如&*p

定义明确的指针操作，例如，p+1

定义明确的指针转换，例如：static_cast<void *>(p)

指针和整型之间的reinterpret_cast, 例如 reninterpret_cast<intptr_t>(p); intptr_t， C++11可选择实现的类型，其长度等于平台上指针的长度。

C++ 11最小垃圾回收支持，基于安全派生指针这个概念，enum class pointer_safety { relaxed, preferred, strict };

relaxed:完全不支持垃圾回收，和C++98/03一样。

preferred:垃圾回收器用于一些辅助功能，例如内存泄露检测或检测对象是否被一个错误的指针解引用。

strict:编译器支持最小垃圾回收以及安全派生指针的概念。

目前还没有编译支持最小垃圾回收。C++11规则通过如下两个api来包裹一段内存，通知垃圾回收器不得回收：
```
    void declare_reachable(void* p);			
    template<class T> T* undeclare_reachable(T *p) noexcept;	
```		
下面语句可以让垃圾回收器不关心从p开始的连续n的内存：
```
    void declare_no_pointers(char*p ,size_t n)noexcept;			
    void undeclare_no_pointers(char*p ,size_t n) noexcept;			
```
## 35. 常量表达式
编译时常量：constexpr

运行时常量: const

## 36. 线程局部存储
线程局部存储变量：拥有线程生命周期及线程可见性的变量。

int thread_local errCode;// 将一个变量声明为thread_local， 其值将在线程开始时被初始化，线程结束时，其值将不再有效。每个线程都将拥有独立的errCode的拷贝，一个线程对errCode的读写并不会影响另外一个线程中的errCode的数据。

对于thread_local变量地址取值（&），只可以获得当前线程中的TLS变量地址。通常TSL变量的读写性能不会高于普通的全局、静态变量。TSL变量的静态、动态分配取决于编译器的实现，C++11标准没有做这方面规定。


C++11 中的lambda 表达式用于定义并创建匿名的函数对象，以简化编程工作。

lambda 表达式的基本构成：
```
[=] () mutable exception ->int 
{
}
```

