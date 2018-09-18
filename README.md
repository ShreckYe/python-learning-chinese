# Python-learning-Chinese
Python学习向导（中文）

*2018年9月18日更新*

大家好，本文是一个中文的Python学习向导，力图尽可能简洁地介绍Python学习从入门到进阶的各方面。

## 安装与设置
### Python安装教程
本文这一部分尚未完成，请暂时先参考[Python 环境搭建 | 菜鸟教程](https://www.runoob.com/python/python-install.html)。  
提示：在安装时勾选“Add to PATH”，可自动完成其中的设置环境变量步骤。

### 使用Pip安装代码库
Pip是Python自带的包管理软件。确保Python安装时已被添加到系统环境变量PATH中，打开命令行（Windows系统需要以管理员运行）输入
```shell
pip ...
```
即可调用pip的各项功能。
安装代码包的基本格式为
```shell
pip install package-name
```
然后等待下载并安装完毕即可。
## 工具
### IDE
IDE全称Integrated Develpment Envrionment即集成开发环境，是一类集编辑、编译、运行、测试等一体的软件工具。

#### [PyCharm](https://www.jetbrains.com/pycharm/)
本文推荐的Python IDE为JetBrains公司的PyCharm，这一IDE的优点在于它强大的代码补全、格式标准化、代码结构分析等功能。

## 库（library）、包（package）、模块（module）
Python的各种优秀的第三方包是Python编程简洁高效的重要原因之一，学会灵活地调包😜对于成为一个熟练的Python使用者至关重要。
### 基本格式
导入一个模块
```python
import module-name
```
导入一个模块的一个变量或函数
```python
from module-name import variable-name-or-function-name
```
导入一个模块的所有变量和函数
```python
from module-name import *
```
### [Python常用库简介](libraries.md)
## 学习方法
### 教程
#### [SoloLearn](https://www.sololearn.com/)
SoloLearn是一个在线学习编程的APP，有Android客户端、iOS客户端和网页版。  
SoleLearn有一个Python入门教程[Python 3 Tutorial](https://www.sololearn.com/Course/Python/)，同时也可以在APP客户端中找到。

#### JetBrains [Python Edu](https://www.jetbrains.com/education/?fromMenu#lang=python&role=learner)
这是JetBrains开发的一个专门用于Python学习的软件插件，需要与上文提到的PyCharm配合使用。若已安装PyCharm，[安装EduTools Plugin](https://www.jetbrains.com/help/education/install-edutools-plugin.html?section=PyCharm)即可。

### 编程练习
“纸上得来终觉浅，绝知此事要躬行。”编程练习是学习一门编程语言最重要的一个环节。

#### [LeetCode](https://leetcode.com/)
在这里向大家推荐一个编程练习网站LeetCode。  
注册账号并登陆后，在“Problems”一栏中便可看到此网站提供的所有问题，打开其中一个，在语言栏中选择“Python”，填写代码，点击“Submit Solution”即可提交，系统会自动检查你的代码是否正确。在正确完成大概10道题之后，你就能基本熟练掌握编程的基本操作。
