---
title: 设计模式
tags: 设计模式
categories: 设计模式
---

## 设计模式概述

- 模式的诞生与定义
  - 模式(`Pattern`)起源于`建筑业`而非软件业
  - 模式之父——美国加利佛尼亚大学环境结构中心研究所所长
    `Christopher Alexander博士`
  - `《A Pattern Language: Towns, Buildings, Construction》`——`253`个建筑和城市规划模式
  - 模式
    - `Context`（模式可适用的前提条件）
    - `Theme或Problem`（在特定条件下要解决的目标问题）
    - `Solution`（对目标问题求解过程中各种物理关系的记述）

- 设计模式的定义
  • 设计模式(`Design Pattern`)
    • 一套`被反复使用的`、`多数人知晓的`、`经过分类目的`、`代码设计经验`的总结
    • 是一种用于对软件系统中不断重现的设计问题的`解决方案`进行`文档化`的技术
    • 是一种`共享专家设计经验`的技术
    • 目的：`为了可重用代码`、`让代码更容易被他人理解`、`提高代码可靠性`


设计模式是`在特定环境下`为解决`某一通用软件设计问题`提供的`一套定制的解决方案`，该方案描述了对象和类之间的相互作用。
```
Design patterns are descriptions of communicating objects and classes that are customized to solve a general design problem in a particular context.
```

设计模式遵循的原则有6个：

**开闭原则（Open Close Principle）**

对扩展开放，对修改关闭。

**1、单一职责原则（Single Responsibility Principle）**

不要存在多于一个导致类变更的原因，也就是说每个类应该实现单一的职责，如若不然，就应该把类拆分。

**2、里氏替换原则（Liskov Substitution Principle）**

只有当派生类可以替换掉基类，软件单位的功能不受到影响时，基类才能真正被复用，而派生类也能够在基类的基础上增加新的行为。

**3、依赖倒转原则（Dependence Inversion Principle）**

这个是开闭原则的基础，对接口编程，依赖于抽象而不依赖于具体。[依赖倒置请看这篇文章](https://cityfire.github.io/2023/08/02/inject/)

**4、接口隔离原则（Interface Segregation Principle）**

使用多个隔离的接口来降低耦合度。

**5、迪米特法则（最少知道原则）（Demeter Principle）**

一个实体应当尽量少的与其他实体之间发生相互作用，使得系统功能模块相对独立。

**6、合成复用原则（Composite Reuse Principle）**

原则是尽量使用合成/聚合的方式，而不是使用继承。继承实际上破坏了类的封装性，超类的方法可能会被子类修改。


## 程序设计目标：高内聚，低耦合


### 设计模式的分类
根据目的可以将设计模式分为如下三种类型：

### 1、创建型(Creational)模式：用于描述“怎样创建对象”。
### 2、结构型(Structural)模式：用于描述如何将类或对象按某种布局组成更大的结构。
### 3、行为型(Behavioral)模式：用于描述类或对象之间怎样相互协作共同完成某些单个对象都无法单独完成的任务，以及怎样分配职责。

根据作用范围，即模式主要是处理类之间的关系还是处理对象之间的关系，可以将设计模式分为两类：

### 1、类模式：用于处理类与子类之间的关系，这些关系通过继承来建立，是静态的，在编译时刻便确定下来了。
### 2、对象模式：用于处理对象之间的关系，这些关系可以通过组合或聚合来实现，在运行时刻是可以变化的，更具动态性。

范围\目的 | 创建型模式 | 结构型模式 | 行为型模式
:-:|:-:|:-:|:-:
类模式 | 工厂方法模式 |（类）适配器模式 | 解释器模式 模板方法模式
对象模式 | 抽象工厂模式 建造者模式 原型模式 单例模式 |（对象）适配器模式 桥接模式 组合模式 装饰模式 外观模式 享元模式 代理模式 | 责任链模式 命令模式 迭代器模式 中介者模式 备忘录模式 观察者模式 状态模式 策略模式 访问者模式

## 创建型模式

**`创建型模式`的主要`关注点`是“`怎样创建对象？`”，它的`主要特点`是“`将对象的创建与使用分离`”。这样可以`降低系统的耦合度`，使用者不需要`关注对象的创建细节`。**

#### 单例(Singleton) ★★★★☆

确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例。

```
public class Singleton {
    private Singleton() {}
    // 主要是使用了 嵌套类可以访问外部类的静态属性和静态方法 的特性
    private static class Holder {
        private static Singleton instance = new Singleton();
    }
    public static Singleton getInstance() {
        return Holder.instance;
    }
}
```

#### 原型(Prototype) ★★★☆☆

原型模式很简单：有一个原型实例，基于这个原型实例产生新的实例，也就是“克隆”了。

`Object` 类中有一个 `clone()` 方法，它用于生成一个新的对象，当然，如果我们要调用这个方法，`Java` 要求我们的类必须先实现 `Cloneable` 接口，此接口没有定义任何方法，但是不这么做的话，在 `clone()` 的时候，会抛出 `CloneNotSupportedException` 异常。
```
protected native Object clone() throws CloneNotSupportedException;
```
`Java` 的克隆是`浅克隆`，碰到对象引用的时候，克隆出来的对象和原对象中的引用将指向同一个对象。通常实现`深克隆`的方法是将对象进行`序列化`，然后再进行`反序列化`。


#### 工厂模式

定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的实例化延迟到其子类。

应用场景

##### 简单工厂

```
public class FoodFactory {

    public static Food makeFood(String name) {
        if (name.equals("noodle")) {
            Food noodle = new LanZhouNoodle();
            noodle.addSpicy("more");
            return noodle;
        } else if (name.equals("chicken")) {
            Food chicken = new HuangMenChicken();
            chicken.addCondiment("potato");
            return chicken;
        } else {
            return null;
        }
    }
}
```
其中，`LanZhouNoodle` 和 `HuangMenChicken` 都继承自 `Food`。

简单地说，简单工厂模式通常就是这样，一个工厂类 `XxxFactory`，里面有一个静态方法，根据我们不同的参数，返回不同的派生自同一个父类（或实现同一接口）的实例对象。
```
我们强调职责单一原则，一个类只提供一种功能，FoodFactory 的功能就是只要负责生产各种 Food。
```

##### 工厂方法(Factory Method) ★★★★★
简单工厂模式很简单，如果它能满足我们的需要，我觉得就不要折腾了。之所以需要引入工厂模式，是因为我们往往需要使用两个或两个以上的工厂。
```
public interface FoodFactory {
    Food makeFood(String name);
}
public class ChineseFoodFactory implements FoodFactory {

    @Override
    public Food makeFood(String name) {
        if (name.equals("A")) {
            return new ChineseFoodA();
        } else if (name.equals("B")) {
            return new ChineseFoodB();
        } else {
            return null;
        }
    }
}
public class AmericanFoodFactory implements FoodFactory {

    @Override
    public Food makeFood(String name) {
        if (name.equals("A")) {
            return new AmericanFoodA();
        } else if (name.equals("B")) {
            return new AmericanFoodB();
        } else {
            return null;
        }
    }
}
```
其中，`ChineseFoodA`、`ChineseFoodB`、`AmericanFoodA`、`AmericanFoodB` 都派生自 `Food`。
客户端调用：
```
public class APP {
    public static void main(String[] args) {
        // 先选择一个具体的工厂
        FoodFactory factory = new ChineseFoodFactory();
        // 由第一步的工厂产生具体的对象，不同的工厂造出不一样的对象
        Food food = factory.makeFood("A");
    }
}
```
虽然都是调用 `makeFood("A")` 制作 `A` 类食物，但是，不同的工厂生产出来的完全不一样。

第一步，我们需要选取合适的工厂，然后第二步基本上和简单工厂一样。

核心在于，我们需要在第一步选好我们需要的工厂。比如，我们有 `LogFactory` 接口，实现类有 `FileLogFactory` 和 `KafkaLogFactory`，分别对应将`日志`写入`文件`和写入 `Kafka` 中，显然，我们客户端第一步就需要决定到底要实例化 `FileLogFactory` 还是 `KafkaLogFactory`，这将决定之后的所有的操作。

虽然简单，不过我也把所有的构件都画到一张图上，这样读者看着比较清晰：
![工厂方法](<images/factoryMethod.png>)


##### 抽象工厂(Abstract Factory) ★★★★★

为创建一组相关或相互依赖的对象提供一个接口，而且无须指定它们的具体类。

当涉及到产品族的时候，就需要引入抽象工厂模式了。

一个经典的例子是造一台电脑。我们先不引入抽象工厂模式，看看怎么实现。

因为电脑是由许多的构件组成的，我们将 `CPU` 和主板进行抽象，然后 `CPU` 由 `CPUFactory` 生产，主板由 `MainBoardFactory` 生产，然后，我们再将 `CPU` 和主板搭配起来组合在一起，如下图：
![抽象工厂](<images/abstractFactory.png>)
这个时候的客户端调用是这样的：
```
// 得到 Intel 的 CPU
CPUFactory cpuFactory = new IntelCPUFactory();
CPU cpu = intelCPUFactory.makeCPU();

// 得到 AMD 的主板
MainBoardFactory mainBoardFactory = new AmdMainBoardFactory();
MainBoard mainBoard = mainBoardFactory.make();

// 组装 CPU 和主板
Computer computer = new Computer(cpu, mainBoard);
```
单独看 `CPU` 工厂和主板工厂，它们分别是前面我们说的工厂模式。这种方式也容易扩展，因为要给电脑加硬盘的话，只需要加一个 `HardDiskFactory` 和相应的实现即可，不需要`修改现有的工厂`。

但是，这种方式有一个问题，那就是如果 `Intel` 家产的 `CPU` 和 `AMD` 产的主板不能兼容使用，那么这代码就容易出错，因为客户端并不知道它们不兼容，也就会错误地出现随意组合。

下面就是我们要说的产品族的概念，它代表了组成某个产品的一系列附件的集合：
![产品族](<images/products.png>)

当涉及到这种产品族的问题的时候，就需要`抽象工厂模式`来支持了。我们不再定义 `CPU` 工厂、主板工厂、硬盘工厂、显示屏工厂等等，我们直接定义电脑工厂，每个电脑工厂负责生产所有的设备，这样能保证肯定不存在兼容问题。
![抽象工厂模式](<images/abstractFactoryPattern.png>)

这个时候，对于客户端来说，不再需要单独挑选 `CPU`厂商、主板厂商、硬盘厂商等，直接选择一家品牌工厂，品牌工厂会负责生产所有的东西，而且能保证肯定是兼容可用的。
```
public static void main(String[] args) {
    // 第一步就要选定一个“大厂”
    ComputerFactory cf = new AmdFactory();
    // 从这个大厂造 CPU
    CPU cpu = cf.makeCPU();
    // 从这个大厂造主板
    MainBoard board = cf.makeMainBoard();
    // 从这个大厂造硬盘
    HardDisk hardDisk = cf.makeHardDisk();

    // 将同一个厂子出来的 CPU、主板、硬盘组装在一起
    Computer result = new Computer(cpu, board, hardDisk);
}
```
当然，抽象工厂的问题也是显而易见的，比如我们要加个显示器，就需要修改所有的工厂，给所有的工厂都加上制造显示器的方法。这有点违反了`对修改关闭，对扩展开放`这个设计原则。

#### 建造者(Builder) ★★☆☆☆

经常碰见的 `XxxBuilder` 的类，通常都是建造者模式的产物。建造者模式其实有很多的变种，但是对于客户端来说，我们的使用通常都是一个模式的：
```
Food food = new FoodBuilder().a().b().c().build();
Food food = Food.builder().a().b().c().build();
```
套路就是先 `new` 一个 `Builder`，然后可以链式地调用一堆方法，最后再调用一次 `build()` 方法，我们需要的对象就有了。

来一个中规中矩的建造者模式：
```
class User {
    // 下面是“一堆”的属性
    private String name;
    private String password;
    private String nickName;
    private int age;

    // 构造方法私有化，不然客户端就会直接调用构造方法了
    private User(String name, String password, String nickName, int age) {
        this.name = name;
        this.password = password;
        this.nickName = nickName;
        this.age = age;
    }
    // 静态方法，用于生成一个 Builder，这个不一定要有，不过写这个方法是一个很好的习惯，
    // 有些代码要求别人写 new User.UserBuilder().a()...build() 看上去就没那么好
    public static UserBuilder builder() {
        return new UserBuilder();
    }

    public static class UserBuilder {
        // 下面是和 User 一模一样的一堆属性
        private String  name;
        private String password;
        private String nickName;
        private int age;

        private UserBuilder() {
        }

        // 链式调用设置各个属性值，返回 this，即 UserBuilder
        public UserBuilder name(String name) {
            this.name = name;
            return this;
        }

        public UserBuilder password(String password) {
            this.password = password;
            return this;
        }

        public UserBuilder nickName(String nickName) {
            this.nickName = nickName;
            return this;
        }

        public UserBuilder age(int age) {
            this.age = age;
            return this;
        }

        // build() 方法负责将 UserBuilder 中设置好的属性“复制”到 User 中。
        // 当然，可以在 “复制” 之前做点检验
        public User build() {
            if (name == null || password == null) {
                throw new RuntimeException("用户名和密码必填");
            }
            if (age <= 0 || age >= 150) {
                throw new RuntimeException("年龄不合法");
            }
            // 还可以做赋予”默认值“的功能
              if (nickName == null) {
                nickName = name;
            }
            return new User(name, password, nickName, age);
        }
    }
}
```
核心是：先把所有的属性都设置给 `Builder`，然后 `build()` 方法的时候，将这些属性复制给实际产生的对象。

看看客户端的调用：
```
public class APP {
    public static void main(String[] args) {
        User d = User.builder()
                .name("foo")
                .password("pAss12345")
                .age(25)
                .build();
    }
}
```
说实话，建造者模式的链式写法很吸引人，但是，多写了很多“无用”的 `builder` 的代码，感觉这个模式没什么用。不过，当属性很多，而且有些必填，有些选填的时候，这个模式会使代码清晰很多。我们可以在 `Builder` 的构造方法中强制让调用者提供必填字段，还有，在 `build()` 方法中校验各个参数比在 `User` 的构造方法中校验，代码要优雅一些。

题外话，强烈建议读者使用 `lombok`，用了 `lombok` 以后，上面的一大堆代码会变成如下这样：
```
@Builder
class User {
    private String  name;
    private String password;
    private String nickName;
    private int age;
}
```
```
怎么样，省下来的时间是不是又可以干点别的了。
```
当然，如果你只是想要链式写法，不想要建造者模式，有个很简单的办法，`User` 的 `getter` 方法不变，所有的 `setter` 方法都让其 `return this` 就可以了，然后就可以像下面这样调用：
```
User user = new User().setName("").setPassword("").setAge(20);
```
```
很多人是这么用的，但是笔者觉得其实这种写法非常地不优雅，不是很推荐使用。
```


## 结构型模式


#### 代理(Proxy) ★★★★☆

为其他对象提供一种代理以控制对这个对象的访问。

`eg`: iOS中经常用代理来委托实现功能


#### 适配器(Adapter) ★★★★☆

将一个类的接口变换成客户端所期待的另一种接口，从而使原本因接口不匹配而无法在一起工作的两个类能够在一起工作。

'eg': 比方一个网络API返回不同的类型，有json、xml、pb这三种格式的数据，可以考虑用适配器模式来封装成一致的调用形式来使用。


#### 装饰器(Decorator) ★★★☆☆

动态地给一个对象添加一些额外的职责。就增加功能来说，装饰器模式相比生成子类更为灵活。


要把装饰模式说清楚明白，不是件容易的事情。也许读者知道 `Java IO` 中的几个类是典型的装饰模式的应用，但是读者不一定清楚其中的关系，也许看完就忘了，希望看完这节后，读者可以对其有更深的感悟。

首先，我们先看一个简单的图，看这个图的时候，了解下层次结构就可以了：
![装饰模式](<images/Decorator.png>)

我们来说说装饰模式的出发点，从图中可以看到，接口 `Component` 其实已经有了 `ConcreteComponentA` 和 `ConcreteComponentB` 两个实现类了，但是，如果我们要增强这两个实现类的话，我们就可以采用装饰模式，用具体的装饰器来装饰实现类，以达到增强的目的。

```
从名字来简单解释下装饰器。既然说是装饰，那么往往就是添加小功能这种，而且，我们要满足可以添加多个小功能。最简单的，代理模式就可以实现功能的增强，但是代理不容易实现多个功能的增强，当然你可以说用代理包装代理的多层包装方式，但是那样的话代码就复杂了。
```

首先明白一些简单的概念，从图中我们看到，所有的具体装饰者们 `ConcreteDecorator***` 都可以作为 `Component` 来使用，因为它们都实现了 `Component` 中的所有接口。它们和 `Component` 实现类 `ConcreteComponent` 的区别是，它们只是装饰者，起装饰作用，也就是即使它们看上去牛逼轰轰，但是它们都只是在具体的实现中加了层皮来装饰而已。


下面来看看一个例子，先把装饰模式弄清楚，然后再介绍下 `Java IO` 中的装饰模式的应用。

最近大街上流行起来了“快乐柠檬”，我们把快乐柠檬的饮料分为三类：红茶、绿茶、咖啡，在这三大类的基础上，又增加了许多的口味，什么金桔柠檬红茶、金桔柠檬珍珠绿茶、芒果红茶、芒果绿茶、芒果珍珠红茶、烤珍珠红茶、烤珍珠芒果绿茶、椰香胚芽咖啡、焦糖可可咖啡等等，每家店都有很长的菜单，但是仔细看下，其实原料也没几样，但是可以搭配出很多组合，如果顾客需要，很多没出现在菜单中的饮料他们也是可以做的。

在这个例子中，红茶、绿茶、咖啡是最基础的饮料，其他的像金桔柠檬、芒果、珍珠、椰果、焦糖等都属于装饰用的。当然，在开发中，我们确实可以像门店一样，开发这些类：`LemonBlackTea`、`LemonGreenTea`、`MangoBlackTea`、`MangoLemonGreenTea`......但是，很快我们就发现，这样子干肯定是不行的，这会导致我们需要组合出所有的可能，而且如果客人需要在红茶中加双份柠檬怎么办？三份柠檬怎么办？

不说废话了，上代码。
首先，定义饮料抽象基类：
```
public abstract class Beverage {
      // 返回描述
      public abstract String getDescription();
      // 返回价格
      public abstract double cost();
}

然后是三个基础饮料实现类，红茶、绿茶和咖啡：
public class BlackTea extends Beverage {
      public String getDescription() {
        return "红茶";
    }
      public double cost() {
        return 10;
    }
}
public class GreenTea extends Beverage {
    public String getDescription() {
        return "绿茶";
    }
      public double cost() {
        return 11;
    }
}
...// 咖啡省略
```
定义调料，也就是装饰者的基类，此类必须继承自 `Beverage`：
```
// 调料
public abstract class Condiment extends Beverage {

}

然后我们来定义柠檬、芒果等具体的调料，它们属于装饰者，毫无疑问，这些调料肯定都需要继承调料 Condiment 类：
public class Lemon extends Condiment {
    private Beverage bevarage;
    // 这里很关键，需要传入具体的饮料，如需要传入没有被装饰的红茶或绿茶，
    // 当然也可以传入已经装饰好的芒果绿茶，这样可以做芒果柠檬绿茶
    public Lemon(Beverage bevarage) {
        this.bevarage = bevarage;
    }
    public String getDescription() {
        // 装饰
        return bevarage.getDescription() + ", 加柠檬";
    }
    public double cost() {
        // 装饰
        return beverage.cost() + 2; // 加柠檬需要 2 元
    }
}

public class Mango extends Condiment {
    private Beverage bevarage;
    public Mango(Beverage bevarage) {
        this.bevarage = bevarage;
    }
    public String getDescription() {
        return bevarage.getDescription() + ", 加芒果";
    }
    public double cost() {
        return beverage.cost() + 3; // 加芒果需要 3 元
    }
}
...// 给每一种调料都加一个类
```
看客户端调用：
```
public static void main(String[] args) {
    // 首先，我们需要一个基础饮料，红茶、绿茶或咖啡
    Beverage beverage = new GreenTea();
    // 开始装饰
    beverage = new Lemon(beverage); // 先加一份柠檬
    beverage = new Mongo(beverage); // 再加一份芒果

    System.out.println(beverage.getDescription() + " 价格：￥" + beverage.cost());
    //"绿茶, 加柠檬, 加芒果 价格：￥16"
}
```
如果我们需要芒果-珍珠-双份柠檬-红茶：
```
Beverage beverage = new Mongo(new Pearl(new Lemon(new Lemon(new BlackTea())))); 
```
是不是很变态？
看看下图可能会清晰一些：
![装饰模式](<images/decoratorPattern.png>)
到这里，大家应该已经清楚装饰模式了吧。

下面，我们再来说说 `Java IO` 中的装饰模式。看下图 `InputStream` 派生出来的部分类：
![](<images/javaDecoratorPattern.png>)

我们知道 `InputStream` 代表了输入流，具体的输入来源可以是文件（`FileInputStream`）、管道（`PipedInputStream`）、数组（`ByteArrayInputStream`）等，这些就像前面奶茶的例子中的红茶、绿茶，属于基础输入流。

`FilterInputStream` 承接了装饰模式的关键节点，它的实现类是一系列装饰器，比如 `BufferedInputStream` 代表用缓冲来装饰，也就使得输入流具有了缓冲的功能，`LineNumberInputStream` 代表用行号来装饰，在操作的时候就可以取得行号了，`DataInputStream` 的装饰，使得我们可以从输入流转换为 `Java` 中的基本类型值。

当然，在 `Java IO` 中，如果我们使用装饰器的话，就不太适合`面向接口编程`了，如：
```
InputStream inputStream = new LineNumberInputStream(new BufferedInputStream(new FileInputStream("")));
```

这样的结果是，`InputStream` 还是不具有读取行号的功能，因为读取行号的方法定义在 `LineNumberInputStream` 类中。

我们应该像下面这样使用：
```
DataInputStream is = new DataInputStream(
                              new BufferedInputStream(
                                  new FileInputStream("")));

```
```
所以说嘛，要找到纯的严格符合设计模式的代码还是比较难的。
```
#### 外观(Facade) ★★★★★

`eg`: 以前搞游戏SDK的时候，就是用这个模式来封装API提供给cp调用的。

#### 桥接(Bridge) ★★★☆☆

理解桥接模式，其实就是理解代码抽象和解耦。

我们首先需要一个桥梁，它是一个接口，定义提供的接口方法。
```
public interface DrawAPI {
   public void draw(int radius, int x, int y);
}
```
然后是一系列实现类：
```
public class RedPen implements DrawAPI {
    @Override
    public void draw(int radius, int x, int y) {
        System.out.println("用红色笔画图，radius:" + radius + ", x:" + x + ", y:" + y);
    }
}
public class GreenPen implements DrawAPI {
    @Override
    public void draw(int radius, int x, int y) {
        System.out.println("用绿色笔画图，radius:" + radius + ", x:" + x + ", y:" + y);
    }
}
public class BluePen implements DrawAPI {
    @Override
    public void draw(int radius, int x, int y) {
        System.out.println("用蓝色笔画图，radius:" + radius + ", x:" + x + ", y:" + y);
    }
}
```
定义一个抽象类，此类的实现类都需要使用 `DrawAPI`：
```
public abstract class Shape {
    protected DrawAPI drawAPI;
    protected Shape(DrawAPI drawAPI) {
        this.drawAPI = drawAPI;
    }
    public abstract void draw();
}
```
定义抽象类的子类：
```
// 圆形
public class Circle extends Shape {
    private int radius;
    public Circle(int radius, DrawAPI drawAPI) {
        super(drawAPI);
        this.radius = radius;
    }
    public void draw() {
        drawAPI.draw(radius, 0, 0);
    }
}
// 长方形
public class Rectangle extends Shape {
    private int x;
    private int y;
    public Rectangle(int x, int y, DrawAPI drawAPI) {
        super(drawAPI);
        this.x = x;
        this.y = y;
    }
    public void draw() {
        drawAPI.draw(0, x, y);
    }
}
```
最后，我们来看客户端演示：
```
public static void main(String[] args) {
    Shape greenCircle = new Circle(10, new GreenPen());
    Shape redRectangle = new Rectangle(4, 8, new RedPen());
    greenCircle.draw();
    redRectangle.draw();
}
```
可能大家看上面一步步还不是特别清晰，我把所有的东西整合到一张图上：

![桥接模式](<images/brigdePattern.png>)

这回大家应该就知道抽象在哪里，怎么解耦了吧。桥接模式的优点也是显而易见的，就是非常容易进行扩展。`有点C++中的友元类和友元函数那味了`。

#### 组合(Composite) ★★★★☆

将对象组合成树形结构以表示“部分-整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性。

`eg`: `文件系统`经常使用。以前我们客户端实现`直播间`里的`礼物系统`中的`礼物面板`，就是使用了`组合模式`来构建不同的`礼物组件`。

#### 享元(Flyweight) ★☆☆☆☆



## 行为型模式


#### 策略(Strategy) ★★★★☆

定义一组算法，将每个算法都封装起来，并且使它们之间可以互换。（多态的一种表现形式）

`eg`: 经常遇到过`if else`这种一坨的条件判断逻辑，这个就可以用`策略模式`来对应不同类型或功能的类来实现。比如登录注册模块验证可以有多种不同的形式，例如`手机号码`，`电子邮箱`、`QQ/Wechat账号`、`Apple账号`、`Fackbook账号`、`Google账号`等，都可以考虑`策略模式`封装使用。

#### 观察者(Observer) ★★★★★

定义对象间一种一对多的依赖关系，使得每当一个对象改变状态，则所有依赖于它的对象都会得到通知并被自动更新。

`eg`: `发布订阅`模式，`组件间的通信方式`也可以考虑采用`观察者模式`。

#### 模板方法(Template Method) ★★★☆☆


#### 迭代器(Iterator) ★★★★★

它提供一种方法访问一个容器对象中各个元素，而又不需暴露该对象的内部细节。


#### 责任链(Chain of Responsibility) ★★☆☆☆

使多个对象都有机会处理请求，从而避免了请求的发送者和接受者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有对象处理它为止。

`eg`: 客户端`事件的传递`，Java中的`过滤器`、`拦截器`等。

#### 命令(Command) ★★★★☆

将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。

`eg`: 电视机的`遥控器`就是典型的`命令模式`实现。

#### 备忘录(Memento) ★★☆☆☆

在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原先保存的状态。

#### 状态(State) ★★★☆☆

当一个对象内在状态改变时允许其改变行为，这个对象看起来像改变了其类。

`eg`:`状态机`

#### 访问者(Visitor) ★☆☆☆☆



#### 中介者(Mediator) ★★☆☆☆

用一个中介对象封装一系列的对象交互，中介者使各对象不需要显示地相互作用，从而使其耦合松散，而且可以独立地改变它们之间的交互。

`eg`:`iOS`、`Android`等移动端平台一般用来`组件化`或`插件化`，解耦合。

#### 解释器(Interpreter) ★☆☆☆☆


### 设计模式的优点

- `融合了众多专家的经验`，并以一种标准的形式供广大开发人员所用。
- 提供了一套`通用的设计词汇和一种通用的语言`，以方便开发人员之间进行沟通和交流，使得设计方案更加通俗易懂。
- 让人们可以更加简单方便地`复用成功的设计和体系结构`。
- 使得设计方案更加`灵活`，且`易于修改`。
- 将提高软件系统的`开发效率和软件质量`，且在一定程度上节约设计成本。
- 有助于初学者更深入地`理解面向对象思想`，方便阅读和学习现有类库与其他系统中的源代码，还可以提高软件的设计水平和代码质量。


## 什么是UML?

1) `UML`，全称`Unified Modeling Language` `UML (统一建模语言)`， 是一种用于软件系统分析和设计的语言工具，它用于帮助软件开发人员进行思考和记录思路的结果。

2) `UML` 类似流程图，本身有一套符号的规定，就像数学符号和化学符号一样，这些符号用于描述软件模型中的各个元素和他们之间的关系，比如`类、接口、实现、泛化、依赖、组合、聚合`等。

`UML图`可以简单分为三类:

### 用例图(`Use Case`)。
### 静态结构图:类图、对象图、包图、组件图、部署图。
### 动态行为图:交互图(时序图与协作图)、状态图、活动图。

### 依赖

### 实现

### 泛化

### 组合 

### 聚合  

认识`UML类图`能更好的的学习设计模式，主流的设计模式都能够通过`UML类图`更加明亮清晰的展示类与类之间的关系；学会`UML类图`也可以更快速的看懂类与类之间的关系。