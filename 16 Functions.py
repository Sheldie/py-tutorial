# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print()


# 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。Python提供了许多内建函数，比如print()。
# 但也可以自己创建函数，这被叫做用户自定义函数。

# 你可以定义一个由自己想要功能的函数，以下是简单的规则：
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

print('Define a function'.center(100, '-'))
# def 函数名（参数列表）:
#     函数体


def hello():
    print("Hello World!")


hello()


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


print('Function call'.center(100, '-'))
# 定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
# 这个函数的基本结构完成以后，可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。


def printme(str):
    # 打印任何传入的字符串
    print(str)
    return


printme("我要调用用户自定义函数!")
printme("再次调用同一函数")


print('Parameter passing'.center(100, '-'))
# 在 python 中，类型属于对象，变量是没有类型的
a = [1, 2, 3]
a = "Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型
# 而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

# 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
# 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

# python 函数的参数传递：
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
# 比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
# python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。


# 传不可变对象实例
def ChangeInt(a):
    a = 10
    print("函数内：", a)


b = 2
ChangeInt(b)
print("函数外：", b)  # 结果是 2

# 实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象
# 在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。


# 传可变对象实例

# 可写函数说明
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


print('Parameter'.center(100, '-'))
# 调用函数时可使用的正式参数类型：必需参数、关键字参数、默认参数、不定长参数


# 必须参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
def printme(str):
    print(str)
    return


# 调用 printme 函数，不加参数会报错
printme('Hello!')
print()
# Traceback (most recent call last):
#   File "test.py", line 10, in <module>
#     printme()
# TypeError: printme() missing 1 required positional argument: 'str'


# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printinfo(name, age):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print()


# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
def printinfo(name, age=35):
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
print()


# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)
print()


# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def printinfo(arg1, *vartuple):
    print("输出: ")
    print('argv: ', arg1)
    for var in vartuple:
        print('tuple: ', var)
    return


# 调用printinfo 函数
printinfo(10)
print("------------------------")
printinfo(70, 60, 50)
print()


# 参数带两个星号 **基本语法
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
def printinfo(arg1, **vardict):
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)
print()


# 声明函数时，参数中星号 * 可以单独出现
def f(a, b, *, c):
    return a + b + c


# 如果单独出现星号 * 后的参数必须用关键字传入。
# print(f(1, 2, 3))
# Traceback (most recent call last):
#   File "D:/Projects/py-tutorital/16 Functions.py", line 212, in <module>
#     print(f(1,2,3))
# TypeError: f() takes 2 positional arguments but 3 were given
print(f(1, 2, c=3))
print()


print('lambda'.center(100, '-'))
# 匿名函数
# python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
print()

print('return'.center(100, '-'))
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)