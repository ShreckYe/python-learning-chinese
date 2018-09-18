# Python-learning-Chinese
Python学习资料（中文）

*2018年9月18日更新

大家好，这里是一些关于Python学习的资料。

## 安装与设置
### [Python安装教程](installation.md)
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
### 编程练习
“纸上得来终觉浅，绝知此事要躬行。”编程练习是学习一门编程语言最重要的一个环节。

在这里向大家推荐一个编程练习网站LeetCode：https://leetcode.com/  
注册账号并登陆后，在“Problems”一栏中便可看到此网站提供的所有问题，打开其中一个，在语言栏中选择“Python”，填写代码，点击“Submit Solution”即可提交，系统会自动检查你的代码是否正确。
