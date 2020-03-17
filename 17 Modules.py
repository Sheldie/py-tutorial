# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import sys


# 在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
# 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
print()
print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\nPython 路径为：', sys.path, '\n')

# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。


# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句
# import module1[, module2[,... moduleN]
# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：

# support.py文件代码
# !/usr/bin/python3
# Filename: support.py

def print_func(par):
    print("Hello : ", par)
    return

# test.py文件代码
# !/usr/bin/python3
# Filename: test.py

# # 导入模块
# import support
#
# 现在可以调用模块里包含的函数了
# support.print_func("Runoob")


# 一个模块只会被导入一次，不管执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。
# 当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
# 这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
# 这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。
# 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量。

# sys.path 输出是一个列表，其中第一项是空串''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录）
# 亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。
# 因此若在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。
# 了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。


# 在解释器的当前目录或者sys.path中的一个目录里面来创建一个fibo.py的文件，代码如下：

# 斐波那契(fibonacci)数列模块

# def fib(n):  # 定义到 n 的斐波那契数列
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
#     print()
#
#
# def fib2(n):  # 返回到 n 的斐波那契数列
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a + b
#     return result
#
# 然后进入Python解释器，使用下面的命令导入这个模块：
# import fibo

# 这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里，只是把模块fibo的名字写到了那里。
# 可以使用模块名称来访问函数：
# >>>fibo.fib(1000)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# >>> fibo.fib2(100)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >>> fibo.__name__
# 'fibo'

# 如果打算经常使用一个函数，你可以把它赋给一个本地的名称：
# >>> fib = fibo.fib
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377


# from … import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
#
# from modname import name1[, name2[, ... nameN]]
# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
#
# >>> from fibo import fib, fib2
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#
# from modname import *
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。


# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果想在模块被引入时，模块中的某一程序块不执行，可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
# 说明：__name__ 与 __main__ 底下是双下划线


# dir() 函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
print(dir(sys))


# 标准模块
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是却能很高效的使用，甚至是系统级调用也没问题。
# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
# 应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串

# >>> import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C> print('Runoob!')
# Runoob!
# C>