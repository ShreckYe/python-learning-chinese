# 中文Python学习指南
本文是一个中文的Python学习向导，力图尽可能简洁全面地介绍Python学习从入门到进阶的各方面。

## 安装与设置
### Python安装教程
本文这一部分尚未完成，请暂时先参考[Python3 环境搭建 | 菜鸟教程](http://www.runoob.com/python3/python3-install.html)。  
提示：在安装时勾选“Add to PATH”，可自动完成其中的设置环境变量步骤。

### [Anaconda](https://www.anaconda.com/)
Anaconda是一个自动包含了很多常用库、支持多版本Python安装、包含很多拓展功能的官方Python替代品。

## 工具
### IDE
IDE全称Integrated Develpment Envrionment即集成开发环境，是一类集编辑、编译、运行、测试等一体的软件工具。

#### [PyCharm](https://www.jetbrains.com/pycharm/)
本文推荐的Python IDE为JetBrains公司的PyCharm，这一IDE的优点在于它强大的代码补全、格式标准化、代码结构分析等功能。
##### 解释器（Interpreter）配置
在使用PyCharm第一次创建项目的时候，你需要为它项目指定解释器，在项目创建成功后也可以在“File - Settings - Project: ... - Project Interpreter”中修改。第一次指定解释器时需要添加一个新的解释器，在添加界面，本文建议初学者若使用官方Python环境则选择“System Interpreter”，若使用Conda则选择“Conda Environment”。
#### 其他推荐IDE
[Sublime Text](https://www.sublimetext.com/)：轻巧通用的可拓展编辑器。  
[Jupyter Notebook](http://jupyter.org/)：置于浏览器中的轻量级编辑器，可编写LaTeX公式。  
[Google Colaboratory](https://colab.research.google.com/)：Google云上的基于Jupyter Notebook的在线IDE，其创立的主要目的是和促进机器学习的研究；可直接使用不需要配置，并可使用Google提供的免费CPU、GPU、TPU资源。（需要VPN）

## 库（library）、包（package）、模块（module）
Python的各种优秀的第三方包是Python编程简洁高效的重要原因之一，学会灵活地调包😜对于成为一个熟练的Python使用者至关重要。
### 使用Pip安装代码包
Pip是Python自带的包管理软件。确保Python安装时已被添加到系统环境变量PATH中，打开命令行（Windows系统需要以管理员运行）输入
```shell
pip ...
```
即可调用pip的各项功能。
以numpy为例，安装代码包的基本格式为
```shell
pip install numpy
```
然后等待下载并安装完毕即可。
### 基本格式
下文以numpy和numpy.array为例，列出了一些与导入包有关的基本代码。  
导入一个模块
```python
import numpy
```
导入一个模块并重命名
```python
import numpy as np
```
导入一个模块的一个变量或函数
```python
from numpy import array
```
导入一个模块的所有变量和函数
```python
from numpy import *
```
### [常用Python库简介](libraries.md)
此文列出了一些常用的Python库。
## 实用技巧
### help函数
使用help函数可以调出模块、类、函数、变量的说明文档，如
```python
import numpy as np

help(np.array)
```
即可调出numpy模块中array（数组）的说明文档。
### type函数
使用type函数可以调出模块、类、函数、变量的类型，示例如下
```
>>> import numpy as np
>>> type(np)
<class 'module'>
>>> type(np.array)
<class 'builtin_function_or_method'>
>>> l = [1, 2, 3]
>>> type(l)
<class 'list'>
>>> a = np.array(l)
>>> type(a)
<class 'numpy.ndarray'>
```
### dir函数
使用dir函数可以以一个列表的方式输出一个空间下的所有名字，可以用它来输出一个包下的所有类、函数、变量的名字，也可以用它输出一个类或对象下的所有方法和属性的名字。
```
>>> import numpy as np
>>> dir(np)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '_UFUNC_API', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_add_newdoc_ufunc', '_arg', '_distributor_init', '_globals', '_mat', '_pytesttester', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'gcd', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'pv', 'quantile', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> dir(np.array)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> a = np.zeros(256)
>>> dir(a)
['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']
```
## 学习方法
### 教程
#### [SoloLearn](https://www.sololearn.com/)
SoloLearn是一个英文的在线学习编程的APP，是本文最为推荐的一个Python学习工具，其平台包含Android客户端、iOS客户端和网页版。  
SoleLearn的[Python 3 Tutorial](https://www.sololearn.com/Course/Python/)是一个Python入门教程，由9个模块和92节课组成，每一节课小巧精炼、讲练结合，包含2~4个小页面，以讲解页面、练习页面循环重复的方式组成——讲解页面均包含介绍与示例，练习页面包含一道选择题或者填空题。
![SoloLearn Python 3 Tutorial](SoloLearn%20Python%203%20Tutorial.png)

SoloLearn的手机APP中有一个Code Playground，无需安装任何环境，你就可以在线写一些简单的程序。你可以利用碎片时间在这里练习。  
除此之外，SoloLearn还有一个关于Python常用的包NumPy的教程：在手机APP上，点击主页最左边的博士帽，便可以查看所有可以学习的话题，包括Python 3和Python NumPy。

本文根据一些初学者的学习情况，整理了一份[疑难点解析](common_difficulties.md)，大家可以在学习的同时参考。

#### [Python3 教程 | 菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)
菜鸟教程是国内一个较好的编程基础入门教程网站，其Python教程分为Python 3基础教程和Python 3高级教程。其中Python 3基础教程内容较为完善适合初学者学习，也适合作为忘记特定功能写法时的参考；Python 3高级教程不需要专门学习，建议在需要使用到相关功能时结合实践学习。

#### Coursera [Python for Everybody Specialization](https://www.coursera.org/specializations/python)
这是Coursera网站首页推荐的一个Python编程课程集合，由美国密西根大学（University of Michigan）提供，包含五个课程，分别涉及编程基础、数据结构、Web数据访问、数据库、数据处理与可视化。你可以注册一个Coursera账号免费观看这些课程，同时也可以在上完课程后付费获取Coursera官方证书。

#### JetBrains [Python Edu](https://www.jetbrains.com/education/?fromMenu#lang=python&role=learner)
这是JetBrains开发的一个专门用于Python学习的软件插件，需要与上文提到的PyCharm配合使用。若已安装PyCharm，[安装EduTools Plugin](https://www.jetbrains.com/help/education/install-edutools-plugin.html?section=PyCharm)即可。

#### 其他视频
[[小甲鱼]零基础入门学习Python](https://www.bilibili.com/video/av4050443)是Bilibili上观看次数最多的一个Python教程系列视频。

### 编程练习
“纸上得来终觉浅，绝知此事要躬行。”编程练习是学习一门编程语言最重要的一个环节。

#### [LeetCode](https://leetcode.com/)
在这里向大家推荐一个编程练习网站LeetCode。  
注册账号并登陆后，在“Problems”一栏中便可看到此网站提供的所有问题，打开其中一个，在语言栏中选择“Python”或“Python 3”，填写代码，点击“Submit Solution”即可提交，系统会自动检查你的代码是否正确。在正确完成大概10道题之后，你就能基本熟练掌握编程的基本操作。

本文挑选了一些[适合初学者的LeetCode问题](leetcode/questions-for-beginners.md)，大家可以从这些问题入门逐渐提高自己的编程技巧。
