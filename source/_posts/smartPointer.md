---
date: 2023-11-04 16:23:26
title: 智能指针
tags: [SmartPointer]
categories: [C++]
---
## 1、智能指针简介
智能指针是存储指向动态内存、对象指针的类，工作机制与C语言指针相同，但会在适当时机自动删除指向的内存或对象。

## 2、auto_ptr
`auto_ptr` 是C++标准库提供的类模板，`auto_ptr`对象通过初始化指向由new创建的动态内存。当`auto_ptr`对象生命周期结束时，其析构函数会将`auto_ptr`对象拥有的动态内存自动释放。即使发生异常，通过异常的栈展开过程也能将动态内存释放。

`auto_ptr`使用注意事项如下：
```
（1）auto_ptr不能共享所有权。
（2）auto_ptr不能指向数组。
（3）auto_ptr不能作为容器的成员。
（4）不能通过赋值操作来初始化auto_ptr。
```
```
#include <memory>
#include <string>
#include <stdio.h>
using namespace std;
 
class Test
{
public:
    Test(const char* c)
    {
        m_buffer = c;
        printf("Constructor, %s\n", m_buffer.c_str());
    }
 
    ~Test()
    {
        printf("DeConstructor, %s\n", m_buffer.c_str());
    }
 
    void print()
    {
        printf("%s\n", m_buffer.c_str());
    }
private:
    string m_buffer;
};
 
int main()
{
    auto_ptr<string> p(new string("HelloWorld."));
    printf("%s\n", p->c_str());
    auto_ptr<Test> pTest(new Test("HelloTest."));
    // auto_ptr<Test> pTest = new Test("HelloTest.");// error
    pTest->print();
}
```

## 3、boost::scoped_ptr
`boost::scoped_ptr`是一个简单的智能指针，能够保证在离开作用域后对象被自动释放。

`boost::scoped_ptr`的实现利用了一个栈上的对象去管理一个堆上的对象，从而使得堆上的对象随着栈上的对象销毁时自动删除，`scoped_ptr`不能拷贝，因此不能转换其所有权的。

`scoped_ptr`使用注意事项如下：

```
（1）不能转换所有权
boost::scoped_ptr所管理对象生命周期仅局限于一个作用域，因此不能转换所有权给其它对象。

（2）不能共享所有权

scoped_ptr将拷贝构造函数和赋值运算符定义为私有的，因此scoped_ptr不能用于STL容器中，因为容器中的push_back操作需要调用scoped_ptr的赋值运算符重载函数，会导致编译失败。

（3）不能用于管理数组对象
scoped_ptr是通过delete来删除所管理对象的，而数组对象必须通过deletep[]来删除，因此boost::scoped_ptr不能管理数组对象，如果要管理数组对象需要使用boost::scoped_array类。

（4）多个boost::scoped_ptr对象不能管理同一个对象。

scoped_ptr对象在离开自己作用域时会调用了自身析构函数，在析构函数内部会调用释放对象，当多个scoped_ptr管理同一个对象时，在离开作用域后，会多次调用delete以释放所管理的对象，从而造成程序运行出错。

（5）boost::scoped_ptr对象可以提前释放所管理对象。
```

`boost::scoped_ptr`通过新生成的无名临时变量，将新地址与旧地址交换，在最后脱离作用域范围，对象消亡，调用析构函数，释放

原先空间，达到不内存泄漏，并且对新空间进行管理。

```
#include <stdio.h>
#include <boost/scoped_ptr.hpp>
#include <vector>
using namespace std;
using namespace boost;
 
class Test
{
public:
    Test(const char* c)
    {
        m_buffer = c;
        printf("Creating Test ..., %s\n", m_buffer.c_str());
    }
 
    void print()
    {
        printf("print Test ..., %s\n", m_buffer.c_str());
    }
 
    ~Test()
    {
        printf("Destroying Test ..., %s\n", m_buffer.c_str());
    }
private:
    string m_buffer;
};
 
int main()
{
    printf("=====Main Begin=====\n");
    {
        scoped_ptr<Test> pTest(new Test("HelloTest"));
        // scoped_ptr<Test> pTest1(pTest);// 拷贝构造
        // scoped_ptr<Test> pTest2 = pTest;// 赋值操作符
        pTest->print();
        Test* test = new Test("HelloTest1");
        pTest.reset(test);
        pTest->print();
        pTest.reset();
 
        vector< scoped_ptr<Test> > vec;
        // vec.push_back(pTest); // error
    }
    printf("===== Main End =====\n");
    return 0;
}
```

## 4、boost::shared_ptr
`boost::shared_ptr`是可以共享所有权的智能指针。如果有多个`shared_ptr`共同管理同一个对象时，只有全部`shared_ptr`与对象脱离关系后，被管理的对象才会被释放。

`boost::shared_ptr`对所管理的对象进行了引用计数，当新增一个`boost::shared_ptr`对对象进行管理时，就将对象的引用计数加1；减少一个`boost::shared_ptr`对对象进行管理时，就将对象的引用计数减1，如果对象的引用计数为0时，delete释放其所占的内存。

`boost::shared_ptr`使用注意事项：

```
（1）避免对shared_ptr所管理的对象的直接内存管理操作，以免造成对象的多次释放

（2）shared_ptr不能对循环引用的对象内存自动管理。

（3）不要构造一个临时的shared_ptr作为函数的参数
```
```
#include <stdio.h>
#include <boost/shared_ptr.hpp>
#include <vector>
using namespace std;
using namespace boost;
 
class Test
{
public:
    Test(const char* c)
    {
        m_buffer = c;
        printf("Creating Test ..., %s\n", m_buffer.c_str());
    }
 
    void print()
    {
        printf("print Test ..., %s\n", m_buffer.c_str());
    }
 
    ~Test()
    {
        printf("Destroying Test ..., %s\n", m_buffer.c_str());
    }
private:
    string m_buffer;
};
 
int main()
{
    shared_ptr<Test> pTest(new Test("HelloTest"));
    pTest->print();
    shared_ptr<Test> pTest2 = pTest;
    pTest2->print();
 
    Test* test = new Test("HelloTest1");
    pTest.reset(test);
    pTest->print();
    pTest.reset();
 
    return 0;
}
```

## 5、boost::weak_ptr
`weak_ptr`是为了配合`shared_ptr`而引入的智能指针，用于弥补`shared_ptr`不足，解决循环引用的问题

`boost::weak_ptr`是`boost::shared_ptr`的观察者对象，当被观察的`boost::shared_ptr`失效后，相应的`boost::weak_ptr`也随之失效。`boost::weak_ptr`只对`boost::shared_ptr`进行引用，而不改变其引用计数，`weak_ptr`的构造不会引起指针引用计数的增加，`weak_ptr`析构也不会引起指针引用计数的减少。

```
#include <stdio.h>
#include <boost/shared_ptr.hpp>
#include <boost/weak_ptr.hpp>
 
int main(int argc, char *argv[])
{
    boost::shared_ptr<int> sp(new int(10));
    boost::weak_ptr<int> wp(sp);
 
    // 测试计数器是否是0
    if (!wp.expired()) 
    {
        // 提升wp到shared_ptr---sp2
        boost::shared_ptr<int> sp2 = wp.lock(); 
        *sp2 = 100;
    }
 
    // shared_ptr置空，weak_ptr失效
    sp.reset();  
    printf("expired= %d\n", wp.expired());    
 
    wp.lock();      
}
```

