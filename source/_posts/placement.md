---
date: 2023-08-04 14:48:27
title: placement new
---
## 一、什么是placement new
`placement new`就是在用户指定的内存位置上（这个内存是已经预先分配好的）构建新的对象，因此这个构建过程不需要额外分配内存，只需要调用对象的构造函数在该内存位置上构造对象即可

语法格式：
```
address：placement new所指定的内存地址
ClassConstruct：对象的构造函数
Object * p = new (address) ClassConstruct(...);
```
优点：

在已分配好的内存上进行对象的构建，构建速度快

已分配好的内存可以反复利用，有效的避免内存碎片问题

## 二、用法
下面与普通的`new`操作符来做比较，演示`placement new`的用法：

普通的new操作符分配一个对象的过程如下：

①使用new分配对象内存（堆中）

②调用对象类的构造函数在该内存地址创建对象

例如：

`int *p = new int(1);`

`placement new`分配一个对象的过程如下：

①使用`new`引用一个已经分配好的内存

②调用对象类的构造函数在该内存地址上创建对象

例如：
```
//先分配一对内存
int* buff = new int;
memset(buff,0,sizeof(int));
 
//此处new的placement new，在buff的内存上构造int对象，不需要分配额外的内存
int *p = new (buff)int(3);
 
std::cout << *p << std::endl; //3
```

## 三、演示案例
```
①测试地址
#include <iostream>
#include <string.h>
 
using std::cout;
using std::cin;
using std::endl;
 
int main()
{
    char *buff=new char[sizeof(int)];
    memset(buff,0,sizeof(buff));
//    std::cout<<"buff address:"<<buff<<std::endl;
 
    int *p1=new(buff) int(1);
    std::cout<<"p1:"<<std::endl;
    std::cout<<"    "<<"address:"<<p1<<std::endl;
    std::cout<<"     "<<"value:"<<*p1<<std::endl;
 
    p1=nullptr;
 
    int *p2=new(buff) int(2);
    std::cout<<"p2:"<<std::endl;
    std::cout<<"    "<<"address:"<<p2<<std::endl;
    std:cout<<"     "<<"value:"<<*p2<<std::endl;
 
    p2=nullptr;
 
    //不要忘记释放内存
    delete [] buff;
    return 0;
}
```

可以看到两个指针都是用了同一块地址的内存 


②测试在内存上创建普通数据类型
```
#include <iostream>
#include <string.h>
#include <new>
 
using std::cin;
using std::cout;
using std::endl;
 
int main()
{
    //先分配一对内存
    int* buff = new int;
    memset(buff,0,sizeof(int));
 
    //此处new的placement new，在buff的内存上构造int对象，不需要分配额外的内存
    int *p = new (buff)int(3);
 
    std::cout << *p << std::endl; //3
 
    return 0;
}

```

如果将代码改为下面所示格式也会产生相同的结果
```
#include <iostream>
#include <string.h>
#include <new>
 
using std::cin;
using std::cout;
using std::endl;
 
int main()
{
    //先分配一对内存
    char* buff = new char[sizeof(int)];
    memset(buff,0,sizeof(buff));
 
    //此处new的placement new，在buff的内存上构造int对象，不需要分配额外的内存
    int *p = new (buff)int(3);
 
    std::cout << *p << std::endl; //3
 
    return 0;
}

```

③测试在内存上创建对象 
```
#include <iostream>
#include <string>
#include <string.h>
 
using std::cout;
using std::cin;
using std::endl;
 
class testClass
{
public:
    testClass(int data):data(data){}
    int getData(){return this->data;}
    void setData(int data){this->data=data;}
private:
    int data;
};
 
 
int main()
{
    //申请一个testClass类大小的动态内存
    char *buff=new char[sizeof(testClass)];
    memset(buff,0,sizeof(buff));
 
    //placement new一个对象
    testClass *myClass=new (buff)testClass(10);
    std::cout<<myClass->getData()<<std::endl;
 
    //使用完之后调用析构函数销毁对象并置空（但是buff动态内存仍存在）
    myClass->~testClass();
    myClass=nullptr;
 
    //在这块内存上再次分配一个对象
    testClass *myClass2=new (buff)testClass(12);
    std::cout<<myClass2->getData()<<std::endl;
    
    //释放对象
    myClass2->~testClass();
    myClass2=nullptr;
 
    //释放动态内存
    delete []buff;
 
    return 0;
}

```

④创建一个对象数组
```
#include <iostream>
#include <string>
 
using std::cout;
using std::cin;
using std::endl;
 
class testClass
{
public:
    testClass(int data):data(data){}
    int getData(){return this->data;}
    void setData(int data){this->data=data;}
private:
    int data;
};
 
 
int main()
{
    //申请10个testClass类大小的动态内存
    char *buff=new char[sizeof(testClass)*10];
    memset(buff,0,sizeof(buff));
 
    //将buff的首地址赋值给一个testClass类
    testClass* start=(testClass*)buff;
 
    //循环
    for(int i=0;i<10;++i){
        new (start+i)testClass(i);//placement new一个testClass对象
        std::cout<<"class"<<i+1<<":"<<(start+i)->getData()<<std::endl;
        (start+i)->~testClass();//使用完之后释放对象（但是动态内存仍存在）
    }
    
    //最后是释放动态内存
    delete [] buff;
    return 0;
}

```

⑤共享内存传递对象

在进程间使用共享内存的时候，C++的`placement new`经常被用到。例如主进程分配共享内容，然后在共享内存上创建C++类对象，然后从进程直接attach到这块共享内容，拿到类对象，直接访问类对象的变量和函数

#### 1.主进程以server的方式启动

分配共享内存

在共享内存上通过placement new创建对象SHMObj

#### 2.从进程以普通方式启动

attach到主进程的共享内存

拿到代表SHMObj对象的指针
