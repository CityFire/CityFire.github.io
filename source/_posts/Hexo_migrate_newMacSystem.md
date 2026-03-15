---
title: Hexo移植新系统
date: 2024-11-12 04:35:22
tags: [Hexo]
categories: Hexo
---

# 更换电脑后，如何迁移 Hexo 博客？

## 1. 迁移本地 hexo 文件夹
需要拷贝原电脑项目文件中的`_config.yml`，`themes`，`source`，`scaffolds`，`package.json`，`.gitignore` 等文件到新电脑新建的文件夹中或者建议直接将原文件夹（删除`node_modules`模块）整个打包拷贝到新电脑上。

## 2. 安装插件

### git 

### npm

#### 1、查看当前的npm镜像设置：npm config list

#### 2、删除镜像设置 npm config delete registry

#### 3、清空缓存 npm cache clean --force

#### 4、设置npm镜像
```
npm config set registry https://registry.npmmirror.com
```

#### 5、查看当前的npm镜像设置：npm config list    
##### npm源切换为官方

```
npm config set registry=https://registry.npmjs.org
```

**如图所示**
![如图所示](images/hexo_npm_config.jpg)

### node

![](images/hexo_component.png)

## 3. 本地Git与Github公钥连接  SSH keys
安装好 git 的目的在于，我们执行命令 `hexo d` 后，能将我们本地文档推送到 GitHub 上，所以需要建立本地 Git 与 Github 的连接，我们通过生成 ssh 公钥，让 GitHub 能够认识我们本地的电脑，具体操作如下：

生成密钥

![](images/hexo_rsa_ssh.jpg)

打开 git bash，输入命令：
```
git config --global user.name "你的用户名"
git config --global user.email "你的邮箱@qq.com"
ssh-keygen -t rsa -C "你的邮箱@qq.com"
```

这里的用户名和邮箱不用纠结，就自己填写就好

执行后面的命令就一路 Enter 就可以，后会生成这个奇怪的图案，记得查看这个红框里的地址，找到这个文件。一般在 `/Users/用户名/.ssh` 目录下（记得显示隐藏文件夹），生成了这个 `id_rsa.pub` 文件，即公钥，我们可以先用记事本打开，把里面的字符串保存一下，一会用到

![](images/hexo_rsa_pub.jpg)

进入 Github 的个人设置界面，找到 `SSH and GPG keys` 选项：


这里选择新建 `SSH key`


点击新增公钥，将之前复制的内容全部粘贴到公钥内容里，公钥名称会自己生成，也可以自己修改，点击添加。

![](images/hexo_github_ssh_key.jpg)


## 4. 安装hexo
在Hexo中的`CityFire.github.io`文件夹下，打开 `git bash`，输入以下命令：
```
npm install hexo-cli -g
npm install hexo-deployer-git --save

```

![](images/hexo_new_blog.jpg)

### 测试环境 test
```
hexo clean && hexo g
```

### 本地服务器测试
```
hexo s
```

### 正式环境 publish
```
hexo clean && hexo g && hexo d
```