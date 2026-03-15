---
date: 2023-11-04 16:26:58
title: Qt线程
categories:
- C++
- Qt
tags:
- C++
- 线程
---

## 技术是为业务服务的，同样多线程使用也是为了解决场景问题的。

在Qt中最多的是用`QThread`，只是`QThread`有两种用法，继承与`QObject::moveToThread`函数。

Qt使用QThread来管理线程。下面来看一个例子：

```
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    QWidget *widget = new QWidget(this);
    QVBoxLayout *layout = new QVBoxLayout;
    widget->setLayout(layout);
    QLCDNumber *lcdNumber = new QLCDNumber(this);
    layout->addWidget(lcdNumber);
    QPushButton *button = new QPushButton(tr("Start"), this);
    layout->addWidget(button);
    setCentralWidget(widget);
    QTimer *timer = new QTimer(this);
    connect(timer, &QTimer::timeout, [=]() {
        static int sec = 0;
        lcdNumber->display(QString::number(sec++));
    });
    WorkerThread *thread = new WorkerThread(this);
    connect(button, &QPushButton::clicked, [=]() {
        timer->start(1);
        for (int i = 0; i < 100000000; i++);
        timer->stop();
    });
}
```
我们的主界面有一个用于显示时间的 LCD 数字面板和一个用于启动任务的按钮。程序的目的是用户点击按钮，开始一个非常耗时的运算（程序中我们以一个 `100000000` 次的循环来替代这个非常耗时的工作，在真实的程序中，这可能是一个网络访问，可能是需要复制一个很大的文件或者其它耗时任务），同时 LCD 开始显示逝去的毫秒数。毫秒数通过一个计时器`QTimer`进行更新。计算完成后，计时器停止。这是一个很简单的应用，也看不出有任何问题。但是当我们开始运行程序时，问题就来了：点击按钮之后，程序界面直接卡死停止响应，直到循环结束才开始重新更新。

有经验的开发者立即指出，这里需要使用线程。这是因为 Qt 中所有界面都是在 UI 线程中（也被称为主线程，就是执行了`QApplication::exec()`的线程），在这个线程中执行耗时的操作（比如那个循环），就会阻塞 UI 线程，从而让界面停止响应。界面停止响应，用户体验自然不好，不过更严重的是，有些窗口管理程序会检测到你的程序已经失去响应，可能会建议用户强制停止程序，这样一来你的程序可能就此终止，任务再也无法完成。所以，为了避免这一问题，我们要使用 QThread 开启一个新的线程：

```
class WorkerThread : public QThread
{
    Q_OBJECT
public:
    WorkerThread(QObject *parent = 0)
        : QThread(parent)
    {
    }
protected:
    void run()
    {
        for (int i = 0; i < 100000000; i++);
        emit done();
    }
signals:
    void done();
};

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    QWidget *widget = new QWidget(this);
    QVBoxLayout *layout = new QVBoxLayout;
    widget->setLayout(layout);
    lcdNumber = new QLCDNumber(this);
    layout->addWidget(lcdNumber);
    QPushButton *button = new QPushButton(tr("Start"), this);
    layout->addWidget(button);
    setCentralWidget(widget);
    QTimer *timer = new QTimer(this);
    connect(timer, &QTimer::timeout, [=]() {
        static int sec = 0;
        lcdNumber->display(QString::number(sec++));
    });
    WorkerThread *thread = new WorkerThread(this);
    connect(thread, &WorkerThread::done, timer, &QTimer::stop);
    connect(thread, &WorkerThread::finished, thread, &WorkerThread::deleteLater);
    connect(button, &QPushButton::clicked, [=]() {
        timer->start(1);
        thread->start();
    });
}
```
注意，我们增加了一个`WorkerThread`类。`WorkerThread`继承自`QThread`类，重写了其`run()`函数。我们可以认为，`run()`函数就是新的线程需要执行的代码。在这里就是要执行这个循环，然后发出计算完成的信号。而在按钮点击的槽函数中，使用`QThread::start()`函数启动一个线程（注意，这里不是`run()`函数）。再次运行程序，你会发现现在界面已经不会被阻塞了。另外，我们将`WorkerThread::deleteLater()`函数与`WorkerThread::finished()`信号连接起来，当线程完成时，系统可以帮我们清除线程实例。这里的`finished()`信号是系统发出的，与我们自定义的`done()`信号无关。

这是 Qt 线程的最基本的使用方式之一（确切的说，这种使用已经不大推荐使用，不过因为看起来很清晰，而且简单使用起来也没有什么问题，所以还是有必要介绍）。代码看起来很简单，不过，如果你认为 Qt 的多线程编程也很简单，那就大错特错了。Qt 多线程的优势设计使得它使用起来变得容易，但是`坑`很多，稍不留神就会被绊住，尤其是涉及到与 QObject 交互的情况。稍懂多线程开发的童鞋都会知道，调试多线程开发简直就是煎熬。下面，我们介绍有关多线程编程的相关内容。

我们要认识两个术语：

* 可重入的`（Reentrant）`：如果多个线程可以在同一时刻调用一个类的所有函数，并且保证每一次函数调用都引用一个唯一的数据，就称这个类是可重入的`（Reentrant means that all the functions in the referenced class can be called simultaneously by multiple threads, provided that each invocation of the functions reference unique data.）`。大多数 C++ 类都是可重入的。类似的，一个函数被称为可重入的，如果该函数允许多个线程在同一时刻调用，而每一次的调用都只能使用其独有的数据。全局变量就不是函数独有的数据，而是共享的。换句话说，这意味着类或者函数的使用者必须使用某种额外的机制（比如锁）来控制对对象的实例或共享数据的序列化访问。
  
* 线程安全`（Thread-safe）`：如果多个线程可以在同一时刻调用一个类的所有函数，即使每一次函数调用都引用一个共享的数据，就说这个类是线程安全的`（Threadsafe means that all the functions in the referenced class can be called simultaneously by multiple threads even when each invocation references shared data.）`。如果多个线程可以在同一时刻访问函数的共享数据，就称这个函数是线程安全的。

进一步说，对于一个类，如果不同的实例可以被不同线程同时使用而不受影响，就说这个类是可重入的；如果这个类的所有成员函数都可以被不同线程同时调用而不受影响，即使这些调用针对同一个对象，那么我们就说这个类是线程安全的。由此可以看出，线程安全的语义要强于可重入。

### QThread的两种基本用法

   **1.继承QThread使用方法：**

  继承`QThread`类，实现其`run()`函数，那么`run`函数里的都是在新线程调用。

   **2.QObject::moveToThread：**

  一个类继承`QObject`，然后使用`QObject::moveToThread（QThread *）`函数，把这个类移动到新的线程中去，然后与主线程全部通过信号槽`Qt::QueuedConnection`或者`Qt::BlockingQueuedConnection`（阻塞调用线程，槽函数执行完毕才继续执行）进行信号槽链接进行线程间通讯，那么信号触发的槽是在新的线程执行的，同样新线程的信号链接的主线程的槽，也是在主线程执行的。但是直接调用函数和`Qt::DirectConnection`链接信号槽的槽函数，是会在直接调用的函数和信号发出的线程中执行的。对于`Qt::AutoConnection`（Qt默认的链接方式）链接的信号槽，如果在一个线程就是`Qt::DirectConnection`，不在一个线程就是`Qt::QueuedConnection`。


   ``注：movetothread底层是依赖Qt时间循环实现的（QCoreApplication::postEvent），所以使用movetothread必须是在开启Qt事件循环的程序中，就是main函数中调用QCoreApplication::exec的程序。``

   ## Qt程序中线程的使用场景

   **1.一次耗时的计算，I/O或者初始化**

   不建议使用`QThread`，建议使用：`QRunnable`和`QThreadPool`结合使用或者直接,`QtConcurrent::run`

   **2.周期性的耗时计算或I/O**

   使用继承`QObject`和`moveToThread`函数的方式，封装到类中，然后后台线程启动驻留，然后信号槽传送计算参数和接收计算的数据。

   **3.程序线程分模块，例如网络和数据库单独在一个线程或者分别的线程设计**

   使用继承`Qobject`和`moveToThread`函数的方式，封装到类中，然后后台线程启动驻留，然后信号槽传送操作命令和取回结果。（注`QWidget`的UI操作只能在主线程的）。

   **4.多个任务执行者，分别的执行，一个调度者**

   每个封装一个类，然后执行者和调度者分线程，数个或者单个执行者一个线程，通过信号槽与调度者交互，用`moveToThread`方式分线程。

   **5.程序中引用其他库，其他库且有独立的事件循环**

   用继承`QThread`的方式，在run中启用其他库的事件循环，需要与主线程交互的部分采用自定义事件和`QCoreApplication::postEvent`方式通讯。