---
title: Kubernetes入门
categories: [Kubernetes, 容器编排]
tags: [K8s, 容器, Docker]
---

Kubernetes（简称K8s）是当前最流行的容器编排平台，掌握它对于现代云原生应用开发至关重要。

# Kubernetes介绍

## 应用部署方式演变

在部署应用程序的方式上，主要经历了三个时代：

### 传统部署

直接，将应用程序部署在物理机上。

- **优点**：简单，不需要其他技术的参与
- **缺点**：不能为应用程序定义资源使用边界，很难合理地分配计算资源，而且程序之间容易产生影响

### 虚拟化部署

可以在一台物理机上运行多个虚拟机，每个虚拟机都是独立的环境。

- **优点**：程序环境不会相互产生影响，提供了一定程度的安全性
- **缺点**：增加了操作系统，浪费了部分资源

### 容器化部署

与虚拟化类似，但是共享了操作系统。

- **优点**：
  - 可以保证每个容器拥有自己的文件系统、CPU、内存、进程空间等
  - 运行应用程序所需要的资源都被容器包装，并和底层基础架构解耦
  - 容器化的应用程序可以跨云服务商、跨Linux操作系统发行版进行部署

![容器化部署](images/k8s.png)

### 容器编排问题

容器化部署方式给我们带来很多便利，但是也会出现一些问题：

- 一个容器故障停机了，怎样让另一个容器立刻启动去替补停机的容器？
- 当并发访问量变大的时候，怎样做到横向扩展容器数量？

这些容器管理的问题统称**容器编排问题**，为了解决这些容器编排问题，产生了一些容器编排软件：

| 工具 | 开发者 | 特点 |
|------|--------|------|
| Swarm | Docker | Docker官方，简单易用 |
| Mesos | Apache | 需要与Marathon结合使用 |
| Kubernetes | Google | 功能强大，社区活跃 |

## Kubernetes简介

Kubernetes是一个全新的基于容器技术的分布式架构领先方案，是谷歌严格保密十几年的秘密武器——Borg系统的开源版本，于2014年9月发布第一个版本，2015年7月发布第一个正式版本。

Kubernetes的本质是一组服务器集群，它可以在集群的每个节点上运行特定的程序，来对节点中的容器进行管理。它的目的是实现资源管理的自动化。

### Kubernetes核心功能

- **自我修复**：一旦某一个容器崩溃，能够在1秒钟左右迅速启动新的容器
- **弹性伸缩**：可以根据需要，自动对集群中正在运行的容器数量进行调整
- **服务发现**：服务可以通过自动发现的形式找到它所依赖的服务
- **负载均衡**：如果一个服务启动了多个容器，能够自动实现请求的负载均衡
- **版本回退**：如果发现新发布的程序版本有问题，可以立即回退到原来的版本
- **存储编排**：可以根据容器自身的需求自动创建存储卷

![Kubernetes架构](images/k8snode.png)

## Kubernetes组件

一个Kubernetes集群主要是由**控制节点（Master）**和**工作节点（Node）**构成，每个节点上都会安装不同的组件。

### Master节点组件

Master是集群的控制平面，负责集群的决策。

| 组件 | 功能描述 |
|------|----------|
| **API Server** | 资源操作的唯一入口，接收用户输入的命令，提供认证、授权、API注册和发现等机制 |
| **Scheduler** | 负责集群资源调度，按照预定的调度策略将Pod调度到相应的Node节点上 |
| **ControllerManager** | 负责维护集群的状态，比如程序部署安排、故障检测、自动扩展、滚动更新等 |
| **Etcd** | 负责存储集群中各种资源对象的信息 |

### Node节点组件

Node是集群的数据平面，负责为容器提供运行环境。

| 组件 | 功能描述 |
|------|----------|
| **Kubelet** | 负责维护容器的生命周期，即通过控制Docker，来创建、更新、销毁容器 |
| **KubeProxy** | 负责提供集群内部的服务发现和负载均衡 |
| **Docker** | 负责节点上容器的各种操作 |

![Kubernetes组件架构](images/13022150_627d503e5e3a681161.webp)

### 组件调用关系

以部署一个Nginx服务为例，说明Kubernetes系统各个组件的调用关系：

1. Kubernetes环境启动后，Master和Node都会将自身的信息存储到Etcd数据库中
2. Nginx服务的安装请求首先被发送到Master节点的API Server组件
3. API Server组件调用Scheduler组件来决定应该把这个服务安装到哪个Node节点上
4. Scheduler从Etcd中读取各个Node节点的信息，按照算法进行选择，将结果告知API Server
5. API Server调用Controller Manager去调度Node节点安装Nginx服务
6. Kubelet接收到指令后，通知Docker，然后由Docker来启动一个Nginx的Pod
7. Pod是Kubernetes的最小操作单元，容器必须运行在Pod中
8.外界用户通过KubeProxy对Pod产生访问的代理来访问Nginx服务

## Kubernetes核心概念

### Master

集群控制节点，每个集群需要至少一个Master节点负责集群的管控。

### Node

工作负载节点，由Master分配容器到这些Node工作节点上，然后Node节点上的Docker负责容器的运行。

### Pod

Kubernetes的最小控制单元，容器都是运行在Pod中的。一个Pod中可以有一个或者多个容器。

**Pod的特点**：
- Pod中的容器共享网络和存储
- Pod是临时的，可能会被销毁和重建
- 通常通过Controller来管理Pod的生命周期

### Controller

控制器，通过它来实现对Pod的管理，比如启动Pod、停止Pod、伸缩Pod的数量等。

**常见的Controller**：

| 类型 | 用途 |
|------|------|
| Deployment | 部署无状态应用 |
| StatefulSet | 部署有状态应用 |
| DaemonSet | 在每个Node上运行一个Pod |
| Job/CronJob | 运行一次性/定时任务 |
| ReplicaSet | 维持Pod副本数 |

### Service

Pod对外服务的统一入口，下面可以维护者同一类的多个Pod。

**Service类型**：
- ClusterIP：集群内部访问
- NodePort：节点端口访问
- LoadBalancer：云负载均衡器
- ExternalName：DNS别名

### Label

标签，用于对Pod进行分类，同一类Pod会拥有相同的标签。

### Namespace

命名空间，用来隔离Pod的运行环境。

**常见的Namespace**：
- default：默认命名空间
- kube-system：系统组件
- kube-public：公开资源

## Pod详解

### Pod的生命周期

Pod的生命周期主要包括以下阶段：

| 阶段 | 描述 |
|------|------|
| Pending | Pod已被创建，但正在被调度 |
| Running | Pod已绑定到Node，所有容器已创建 |
| Succeeded | 所有容器成功终止 |
| Failed | 容器异常退出 |
| Unknown | Pod状态未知 |

### Pod配置示例

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.19
    ports:
    - containerPort: 80
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
      requests:
        memory: "64Mi"
        cpu: "250m"
```

## Deployment详解

### 什么是Deployment？

Deployment是Kubernetes最常用的Workload，用于管理无状态的Pod应用。

### Deployment配置示例

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.19
        ports:
        - containerPort: 80
        resources:
          limits:
            memory: "128Mi"
            cpu: "500m"
```

### 滚动更新

Deployment支持滚动更新，可以平滑地升级应用版本：

```bash
# 查看部署状态
kubectl rollout status deployment/nginx-deployment

# 查看历史版本
kubectl rollout history deployment/nginx-deployment

# 回滚到上一个版本
kubectl rollout undo deployment/nginx-deployment

# 回滚到指定版本
kubectl rollout undo deployment/nginx-deployment --to-revision=2
```

## Service详解

### Service配置示例

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: ClusterIP
```

### Service类型详解

| 类型 | 描述 |
|------|------|
| ClusterIP | 默认类型，仅集群内部可访问 |
| NodePort | 在每个Node上开放一个端口 |
| LoadBalancer | 使用云提供商的负载均衡器 |
| ExternalName | 将服务映射到DNS名称 |

## 常用命令

### Pod命令

```bash
# 查看Pod
kubectl get pods

# 查看Pod详情
kubectl get pods -o wide

# 查看Pod日志
kubectl logs nginx-pod

# 进入Pod容器
kubectl exec -it nginx-pod -- /bin/sh

# 删除Pod
kubectl delete pod nginx-pod
```

### Deployment命令

```bash
# 创建Deployment
kubectl apply -f deployment.yaml

# 查看Deployment
kubectl get deployment

# 扩缩容
kubectl scale deployment nginx-deployment --replicas=5

# 更新镜像
kubectl set image deployment/nginx-deployment nginx=nginx:1.20
```

### Service命令

```bash
# 创建Service
kubectl apply -f service.yaml

# 查看Service
kubectl get service

# 删除Service
kubectl delete service nginx-service
```

### 集群命令

```bash
# 查看节点
kubectl get nodes

# 查看集群信息
kubectl cluster-info

# 查看资源使用
kubectl top nodes
kubectl top pods
```

## 资源清单（YAML）常用字段

### 常用字段解释

| 字段 | 描述 |
|------|------|
| apiVersion | API版本 |
| kind | 资源类型 |
| metadata | 元数据 |
| spec | 规格/期望状态 |
| status | 当前状态（只读） |

### 常用命令

```bash
# 生成YAML模板
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > nginx.yaml

# 查看资源详细信息
kubectl explain pod

# 查看资源JSON结构
kubectl get pod nginx-pod -o json
```

## 总结

Kubernetes作为容器编排领域的标准，提供了强大的容器管理能力：

| 核心功能 | 说明 |
|----------|------|
| 自我修复 | 自动重启失败的容器 |
| 弹性伸缩 | 根据负载自动调整Pod数量 |
| 服务发现 | 自动服务注册与发现 |
| 负载均衡 | 多副本自动负载分发 |
| 版本回滚 | 轻松回退到历史版本 |
| 存储编排 | 动态挂载存储卷 |

掌握Kubernetes的基本概念、核心组件和常用命令，是现代云原生开发者的必备技能。
