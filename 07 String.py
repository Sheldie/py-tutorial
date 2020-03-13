# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

str = 'Hello World!'

# 输出完整字符串
print(str)
# 输出字符串中的第一个字符
print(str[0])
# 输出字符串中第三个至第六个之间的字符串
print(str[2:5])
# 输出从第三个字符开始的字符串
print(str[2:])
# 输出字符串两次
print(str * 2)
# 输出连接的字符串
print(str + "TEST")

print()
# 单词 句子 段落
word = 'word'
sentence = "This is a sentence."
paragraph = """
*****************
    测试 test
*****************
"""
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""


print(word)
print(sentence)
print(paragraph)
print(para_str)


print()
var1 = 'Hello World!'
var2 = "Python Runoob"
num = "123456789"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])
print("var2[1:5]: " + var2[1:5])

# Python列表截取可以接收第三个参数，参数作用是截取的步长
# 以下实例在索引 1 到索引 9 的位置
# 并设置为步长为 2（间隔一个位置）来截取字符串
print(num[1:9:2])
print(num[1:8:3] + "\a")    # 响铃符


print()
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[-1] 输出结果：", a[-1])
print("a[1:4] 输出结果：", a[1:4])
print("a[1:-2] 输出结果：", a[1:-2])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")


print()
# r: 不转义特殊字符
print(r'\n')
print(R'\n')


print()
# 字符串格式化
# 与 C 中 sprintf 函数一样的语法
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
name = 'Runoob'
print('Hello %s' % name)    # 替换变量
# f-string：字面量格式化字符串
print(f'Hello {name}')
print(f'{1+2}')
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')
# 无需判断使用 %s 还是 %d
x = 1
print(f'{x+1}') # Python 3.6
x = 1
# print(f'{x+1=}')  # Python 3.8
# 'x+1=2'



