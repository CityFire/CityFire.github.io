---
title: spring和springMVC的整合笔记
---
## 1、不整合：需要将spring所管理的内容都交给springMVC管理，这样会造成业务逻辑混乱
## 2、整合：spring的配置文件什么时候加载？怎么加载？
解决方法：监听器，可以在ServletContext加载时，通过监听器加载spring的配置文件，创建spring容器
spring提供的监听器：ContextLoaderListener

## 3、bean被创建两次的问题：在springMVC中只扫描控制层，在spring中，通过包含或排除对所扫描的包进行指定

## 4、spring和springMVC的关系
spring是父容器
springMVC是子容器

规定：子容器能够调用访问父容器中的bean，而父容器不能够调用访问子容器中的bean

springMVC             spring
controller———-service———dao

```
spring: Root WebApplicationContext: startup date[]; root of context hierarchy
springMVC: WebApplicationContext for namespace ‘springDispatcherServer’: startup date[]; parent: Root WebApplicationContext


七月 13, 2022 11:39:34 下午 org.apache.catalina.core.StandardContext listenerStop
严重: 例外情况发送上下文删除事件[org.springframework.web.context.ContextLoaderListener]，以便列表实例
java.lang.IllegalStateException: BeanFactory not initialized or already closed - call 'refresh' before accessing beans via the ApplicationContext
	at org.springframework.context.support.AbstractRefreshableApplicationContext.getBeanFactory(AbstractRefreshableApplicationContext.java:170)
```

错误原因：
```
spring配置找不着
spring配置文件还没有创建
spring配置文件出现语法错误
```

默认在WEB-INF文件夹下 applicationContext.xml

错误：
```
<!--  <listener>
    <listener-class>com.wjc.listener.SpringListener</listener-class>
  </listener> -->
  <listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
  
  <!-- <context-param>
     <param-name>contextConfigLocation</param-name>
     <param-value>classpath:spring.xml</param-value>
  </context-param> -->
```

正确:

配置文件放在WEB-INF文件夹下 applicationContext.xml

```
<listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
```
or

需要创建SpringListener文件  创建监听类
```
<listener>
    <listener-class>com.wjc.listener.SpringListener</listener-class>
  </listener>
```
or
```
<listener>
    <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
  </listener>
  
  <context-param>
     <param-name>contextConfigLocation</param-name>
     <param-value>classpath:spring.xml</param-value>
  </context-param>
```




java.lang.IllegalStateException: Neither BindingResult nor plain target object for bean name 'command' available as request attribute
