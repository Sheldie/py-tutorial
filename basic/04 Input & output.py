# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import math


print('hello')

x = 1
y = 2

# 换行输出
print(x)
print(y)

# 不换行输出
name = "qwertyuiop"
i = len(name)   # 字符串长度
while i > 0:    # 字符串逆序输出
    i -= 1
    print(name[i], end="")
print('\n')     # 换两行


s = 'Hello, Shezzer'

str(s)
# 函数返回一个用户易读的表达形式。
repr(s)
# 产生一个解释器易读的表达形式。

str(1/9)

x = 10 * 3.25
y = 200 * 200
s1 = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
# s2 = 'x 的值为： ' + x + ',  y 的值为：' + y + '...'
# print()内的“+”前后数据类型需保持一致
# TypeError: can only concatenate str (not "float") to str

print(s1)
# print(s2)

# repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hello)
print(hellos)

# repr() 的参数可以是 Python 的任何对象
test = repr((x, y, ('Google', 'Shezzer')))
print(test)

print()
# 输出一个平方与立方的表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')    # 注意 'end' 的使用
    print(repr(x*x*x).rjust(4))

# rjust() 右对齐
# str.rjust(width[, fillchar])
# 将字符串靠右，并在左边填充空格。
# 还有类似的方法如 ljust() 和 center()。
# 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

print()
# ljust() 左对齐
for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), end=' ')    # 注意 'end' 的使用
    print(repr(x*x*x).ljust(4))

print()
# 字符串用法
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))     # 见str.format()：0 1 2指位置

print()
# zfill()：在数字的左边填充 0
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print()
# str.format()
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))

# format() 中使用了关键字参数
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 位置及关键字参数可以任意结合，关键字参数必须在最后
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', other='Runoob', 'Taobao'))
# SyntaxError: positional argument follows keyword argument


print()
# import math
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))

# 可选项 : 和格式标识符可以跟着字段名,允许对值进行更好的格式化。
# 将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))


# 输入
str = input("请输入：");
print("你输入的内容是: ", str)




