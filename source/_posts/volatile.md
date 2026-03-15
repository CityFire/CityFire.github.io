---
date: 2023-08-01 14:24:43
title: volatile关键字
categories:
  - C/C++
tags:
  - 多线程
  - 并发
---
# 什么是volatile关键字？
`volatile`关键字是C/C++中的一个关键字，用于告诉编译器：这个变量可能会被其他线程修改，因此在每次使用这个变量时，都应该从内存中重新读取，而不是使用寄存器中的值。
<!-- more -->
# volatile关键字的作用
被 `volatile` 修饰的变量，在对其进行读写操作时，会引发一些可观测的副作用。而这些可观测的副作用，是由程序之外的因素决定的。

# volatile关键字的应用
`volatile`关键字可以用于以下场景：
- 多线程编程：当多个线程共享一个变量时，`volatile`关键字可以确保变量的值在每个线程中都是最新的。
- 中断处理：在中断处理程序中，`volatile`关键字可以确保变量的值在中断处理程序中是最新的。
- 硬件寄存器：当访问硬件寄存器时，`volatile`关键字可以确保变量的值在每次访问时都是最新的。  

## （1）并行设备的硬件寄存器（如状态寄存器）。 假设要对一个设备进行初始化，此设备的某一个寄存器为0xff800000。
```
int  *output = (unsigned  int *)0xff800000; //定义一个IO端口；  
int   init(void)  
{  
    int i;  
    for(i=0;i< 10;i++)
    {  
    *output = i;  
    }  
}
```
经过编译器优化后，编译器认为前面循环半天都是废话，对最后的结果毫无影响，因为最终只是将output这个指针赋值为 9，所以编译器最后给你编译编译的代码结果相当于：
```
int  *output = (unsigned  int *)0xff800000; //定义一个IO端口；
int   init(void)	
{
    *output = 9;
}
```
如果你对此外部设备进行初始化的过程是必须是像上面代码一样顺序的对其赋值，显然优化过程并不能达到目的。反之如果你不是对此端口反复写操作，而是反复读操作，其结果是一样的，编译器在优化后，也许你的代码对此地址的读操作只做了一次。然而从代码角度看是没有任何问题的。这时候就该使用volatile通知编译器这个变量是一个不稳定的，在遇到此变量时候不要优化。

## （2）一个中断服务子程序中访问到的变量；
```
static  int  i = 0;
int main()
{
    while(1)
    {
    if(i) dosomething();
    }
}

/* Interrupt service routine */
void IRS()
{
	i=1;
}

```
上面示例程序的本意是产生中断时，由中断服务子程序IRS响应中断，变更程序变量i，使在main函数中调用dosomething函数，但是，由于编译器判断在main函数里面没有修改过i，因此可能只执行一次对从i到某寄存器的读操作，然后每次if判断都只使用这个寄存器里面的“i副本”，导致dosomething永远不会被调用。如果将变量i加上volatile修饰，则编译器保证对变量i的读写操作都不会被优化，从而保证了变量i被外部程序更改后能及时在原程序中得到感知。

## （3）多线程应用中被多个任务共享的变量。
当多个线程共享某一个变量时，该变量的值会被某一个线程更改，应该用 volatile 声明。作用是防止编译器优化把变量从内存装入CPU寄存器中，当一个线程更改变量后，未及时同步到其它线程中导致程序出错。volatile的意思是让编译器每次操作该变量时一定要从内存中真正取出，而不是使用已经存在寄存器中的值。示例如下：
```
volatile  bool  bStop = false; // bStop 为共享全局变量  
// 第一个线程：
void threadFunc1()
{
    ...
    while(!bStop){...}
}
// 第二个线程终止上面的线程循环
void threadFunc2()
{
    ...
    bStop = true;
}
```

要想通过第二个线程终止第一个线程循环，如果bStop不使用volatile定义，那么这个循环将是一个死循环，因为bStop已经读取到了寄存器中，寄存器中bStop的值永远不会变成FALSE，加上volatile，程序在执行时，每次均从内存中读出bStop的值，就不会死循环了。

是否了解volatile的应用场景是区分C/C++程序员和嵌入式开发程序员的有效办法，搞嵌入式的家伙们经常同硬件、中断、RTOS等等打交道，这些都要求用到volatile变量，不懂得volatile将会带来程序设计的灾难。

# volatile常见问题

下面的问题可以看一下面试者是不是真正了解volatile。 
（1）一个参数既可以是const还可以是volatile吗？为什么？ 可以。一个例子是只读的状态寄存器。它是volatile因为它可能被意想不到地改变。它是const因为程序不应该试图去修改它。

（2）一个指针可以是volatile吗？为什么？ 可以。尽管这并不常见。一个例子是当一个中断服务子程序修改一个指向一个buffer的指针时。

（3）下面的函数有什么错误？
```
int square(volatile int *ptr)
{
    return *ptr * *ptr;
}
```
这段代码的有个恶作剧。这段代码的目的是用来返指针ptr指向值的平方，但是，由于ptr指向一个volatile型参数，编译器将产生类似下面的代码：
```
int square(volatile int *ptr)	
{
    int a, b;
    a = *ptr;
    b = *ptr;
    return a * b;
}
```
由于*ptr的值可能被意想不到地该变，因此a和b可能是不同的。结果，这段代码可能返不是你所期望的平方值！正确的代码如下：
```
long square(volatile int *ptr)
{
    int a;
    a = *ptr;
    return a * a;
}
```

# volatile使用

- `volatile` 关键字是一种类型修饰符，用它声明的类型变量表示可以被某些编译器未知的因素（操作系统、硬件、其它线程等）更改。所以使用 `volatile` 告诉编译器不应对这样的对象进行优化。

- `volatile` 关键字声明的变量，每次访问时都必须从内存中取出值（没有被 `volatile` 修饰的变量，可能由于编译器的优化，从 CPU 寄存器中取值）

- `const` 可以是 `volatile` （如只读的状态寄存器）

- 指针可以是 `volatile`


# 番外篇（多线程编程中的volatile）

volatile可能不是为多线程而生，但在多线程编程时，却可以加以利用。而且说实话，还是挺有用的!

至于强调“`volatile`和多线程没有关系x3”，我觉得没必要吧？至少从逻辑上讲，话说得太满就比较容易证伪。真的完全没关系吗？

我在和人讨论时，最长听到的言论是：`volatile`不能保证线程安全，所以怎么怎么样。可是线程安全到底是什么？又有什么东西能对线程安全（或者说并发安全）提供一揽子解决方案？依我看，`volatile`与很多人喜欢挂嘴边上的`memory fence`，在多线程编程时都有用，它们解决不同的问题。

`volatile`就是提示编译器避免对特定变量的操作进行优化。最简单粗暴的理解就是：一个int，在有些时候，它可以由一个通用寄存器全权代表，比如eax或者rax。一开始把这个int的值从mem里加载到eax/rax中后，可能在一段时间内不用再去碰mem里的int，直接操作这个ax寄存器就好了，这样做能快些。一个典型的例子就是一个仅用于循环计数器的变量。而volatile就是告诉编译器：你别给我这么干，有些事情你不懂。

然而这和多线程有关系吗？有证据吗？特定情况下会有。特定情况举例如下：
参考下面的乡土版自旋锁：
```
class Test {
    /*volatile*/ int flag;
public:
    Test(void) :flag(0) {}

    void spinWait(void) {
        while (0 == flag);
    }

    void signal(void) {
        flag = 1;
    }
};
```
`Test::spinWait()`被调用后会进入“死循环”直到`Test::signal()`被调用，flag变量被置为1为止，这没错吧？
现在我们在同一个cpp文件里补全代码（同一个文件，免得你觉得我们在晃点编译器），在`main`函数里开两个线程，一个调用`spinWait`死等，另一个延迟10秒后解放前者：
```
void* thread_spinner(void *param) {
    cout << "thread_spinner: waiting..." << endl;
    ((Test*)param)->spinWait();
    cout << "thread_spinner: quit" << endl;
    return 0;
}

void* thread_shouter(void *param) {
    cout << "thread_shouter: setting signal in 10 secs..." << endl;
    sleep(10);
    ((Test*)param)->signal();
    cout << "thread_shouter: quit" << endl;
    return 0;
}

int main(int argc, char* argv[]) {
    Test testObj;
    pthread_t threads[2];
    pthread_create(threads + 0, NULL, thread_spinner, &testObj);
    pthread_create(threads + 1, NULL, thread_shouter, &testObj);
    for(int i = 0; i < 2; i++)
        pthread_join(threads[i], NULL);
    return 0;
}
```
可是这样行吗？有可能行，也有可能不行。在g++里面，`-O0`下可以，`-O1`就不可以了。
假如你把上面两段贴到一个cpp里，然后用下面Makefile去编译：
```
CC=g++
CCFLAGS=-c -fno-inline -O1
CL=g++
CLFLAGS=-lpthread

all: testvola.exe testvola.asm

testvola.exe: testvola.o
	${CL} -o $@ $< ${CLFLAGS}

testvola.o: testvola.cpp
	${CC} ${CCFLAGS} -g -o $@ $<

testvola.asm: testvola.cpp
	${CC} ${CCFLAGS} -S -masm=intel -o $@ $<

.PHONY: clean

clean:
	rm -f *.o *.exe *.s *.asm
```
然后运行生成的`testvola.exe`文件，程序会卡死：
```
wjc-MacBook-Pro:~/testvola$ ./testvola.exe 
thread_spinner: waiting...
thread_shouter: setting signal in 10 secs...
thread_shouter: quit
^C   <<<< 卡死在这里了，只能ctrl+c杀掉
wjc-MacBook-Pro:~/testvola$ uname -a
Linux wjc-MacBook-Pro 4.15.0-117-generic #118-Ubuntu SMP Fri Sep 4 20:02:41 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
wjc-MacBook-Pro:~/testvola$ 
```
为什么会这样？`spinWait`里明明在不停的读`flag`变量，难道`signal`函数没有改变它的值吗？
`侯捷`老师在源码剖析里说过，源码面前了无秘密。你看看`spinWait`函数编译后的代码，真相很清晰：
```
_ZN4Test8spinWaitEv:
.LFB1556:
	.cfi_startproc
	mov	eax, DWORD PTR [rdi]
.L10:                       <<<<< 看这里
	test	eax, eax    <<<<< 看这里
	je	.L10        <<<<< 看这里
	rep ret
	.cfi_endproc
.LFE1556:
	.size	_ZN4Test8spinWaitEv, .-_ZN4Test8spinWaitEv
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"thread_spinner: waiting..."
.LC1:
	.string	"thread_spinner: quit"
	.text
	.globl	_Z14thread_spinnerPv
	.type	_Z14thread_spinnerPv, @function
```
`signal`函数不用看了，`spinWait`在这里只跟`eax`较劲，正常情况下，别的线程不能改变`spinWait`线程的寄存器值，不论是单核还是多核。
如果你耐着性子看到这里，还说“volatile跟多线程没关系”吗？还不信的话，那我们把上面代码中，被注释掉的`/*volatile*/`改回来，重新编译再试试：
```
 class Test {
    volatile int flag;
public:
......
```
看`spinWait`函数的编译结果：
```
_ZN4Test8spinWaitEv:
.LFB1556:
	.cfi_startproc
.L10:
	mov	eax, DWORD PTR [rdi]    <<<< 看这里!
	test	eax, eax
	je	.L10
	rep ret
	.cfi_endproc
.LFE1556:
	.size	_ZN4Test8spinWaitEv, .-_ZN4Test8spinWaitEv
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"thread_spinner: waiting..."
.LC1:
	.string	"thread_spinner: quit"
	.text
	.globl	_Z14thread_spinnerPv
	.type	_Z14thread_spinnerPv, @function
```
看到多出来的那个指令了吗？那就是关键。那是增加`volatile`前后在结果里反应出来的唯一变化，基于逻辑推断只能是`volatile`起到的作用。运行一下试试：
```
wjc-MacBook-Pro:~/testvola$ ./testvola.exe 
thread_spinner: waiting...
thread_shouter: setting signal in 10 secs...
thread_shouter: quitthread_spinner: quit

wjc-MacBook-Pro:~/testvola$ 
```
终于看到`“thread_spinner: quit”`了。
当然了，自旋锁有可能不必非要这样设计实现，所以volatile是解决这个问题的有效方法，但未必是唯一方法（所以我的话可没有说满）。但这毕竟也不是一个无理取闹的实现方法，实际上它简单有效，老幼咸宜，谁都能一眼看懂，我觉得还挺好的。
我说完了。
哦对，最后针对有人说`mutex`，我补充一点：你知道为啥有`mutex`还要用`busy loop`来实现锁吗？你知道在CPU的世界里，进出一次内核级等待，已经从春秋到了汉唐。

还有人说volatile最初就是针对外设向内存读写数据而引入的。拜托，为外设而引入到x86系统里的设计叫DMA，最早是`英特尔`的8237芯片。其实我并不反对volatile最初不是给多线程设计的，但是我认为不要去过份关注它的“血统”，而要看它所给程序带来的变化，能不能帮我们解决眼下的问题。




