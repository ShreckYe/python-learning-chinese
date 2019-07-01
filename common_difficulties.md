# Python 疑难点解析（按 SoloLearn Python 3 Tutorial 结构整理）
## 第一章（Basic Concepts）
### 类型
Python的所有值都是有类型的，常用的类型为整型`int`、浮点数`float`、字符串`str`。两个值可能使用`print`输出的结果相同，但其类型不同。在分析代码中变量的运算之前，需先弄清楚变量的类型。

## 第二章（Control Structures）
### 比较运算符号、布尔值与if（初学者常见难点）
数学中的比较关系符号（小于`<`、等于`==`、大于`>`）在编程中是运算符号，其运算结果为一个布尔值（`True`、`False`）。看起来像是数学中比较表达式的表达式，实际上是一个运算式，其运算结果即为表示此表达式是否满足的布尔值。

if表达式判断的实际上不是一个关系表达式（虽然很多时候看起来是一个表达式），而是其运算出来的布尔值结果——若结果为`True`，则继续运行if块中的内容；若结果为`False`，则跳过if块中的内容。因此，if的判断表达式可以直接为`True`或`False`，这一点在调试和测试程序中很有用。对于`while`同理。

### 赋值（`=`）与等于（`==`）
`=`并不是表示数学中的等于，而是赋值符号，因此可以出现类似`x = x + 1`这种看起来是在数学中并不成立的方程式的赋值表达式。

`==`是用于判断两个值是否相等的运算符号，如上文所讲，其结果为一个布尔值。在判断两个值是否相等时，应特别注意它们的类型是否相同——存在自动转换关系的不同类型的值是可能相等的（如`bool`、`int`和`float`，比如`False == 0`、`True == 1`、`1 == 1.0`的结果为`True`），但不存在自动转换关系的不同类型的值则一定是不相等的（如任意数值都不与任意字符串相等，比如`1 == "1"`的结果为`False`）。

### 补充：三元运算符
内容只有单行的`if-else`语句块可以使用三元运算符简写在一行中，其格式为
```python
value_1 if bool_exp else value_2
```

如下文的`bool_to_int`函数可以用三元运算符简写为：
```python
def bool_to_int(b):
    return 1 if b else 0

```

附：其他语言的三元运算符略有不同，如：  
C语言/C++/Java：
```
bool_exp ? value_1 : value_2
```
Kotlin：
```kotlin
if (bool_exp) value_1 else value_2
```

## 第三章（Functions & Modules）
### 使用return进行流程控制
`return`表示函数返回并指定返回值。若`return`成功执行，则其后的代码均不会执行，因此在某些时候可以使用`if`和`return`代替`if-elif-else`进行程序流程控制。

如
```python
def bool_to_int(b):
    if b:
        return 1
    else:
        return 0

```
等价于
```python
def bool_to_int(b):
    if b:
        return 1
    
    return 0

```

## 第五章（More Types）
第五章的类型均对应特定的数据结构，若想要根据目的合理选择一个数据类型，则需要了解一些基础的数据结构知识。

这些类型的对应如下，你通过互联网学习这些数据结构的基础知识。。

Python类型 | Python官方名字 | 数据结构
--- | --- | ---
`list` | list (列表) | 列表/数组
`tuple` | tuple (元组) | 数组
`dict` | dictionary (字典) | 哈希表
`set` | set (集合) | 哈希表
`str` | string (字符串) | 列表/数组

## 第六章（Functional Programming）
函数式编程是使用Python语言写出更简洁程序的重要工具，在数据处理相关工作中使用尤其频繁。
