# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print('if'.center(100, '-'))
# if

# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3

# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。

if True:
    print("True")
else:
    print("False")

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
age = 2
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

# 操作运算符
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)

# num = int(input("输入一个数字："))
num = 6
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")


print('while'.center(100, '-'))
# while
# while 判断条件(condition)：
#     执行语句(statements)……

n = 100
s = 0
counter = 1
while counter <= n:
    s = s + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, s))

# 无限循环
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
# print("Good bye!")

# while 循环使用 else 语句
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>
count = 0
while count < 5:
   print(count, "小于 5")
   count = count + 1
else:
   print(count, "大于或等于 5")

# 如果while循环体中只有一条语句，可以将该语句与while写在同一行中


print('for'.center(100, '-'))
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x, end=" ")
print()

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# 需要遍历数字序列，可以使用内置range()函数。它会生成数列。
for i in range(5):
    print(i, end=" ")
print()

for i in range(5, 9):   # 左闭右开
    print(i, end=" ")
print()

for i in range(0, 10, 3):   # 步长
    print(i, end=" ")
print()

for i in range(-10, -100, -30):
    print(i, end=" ")
print('\n')

# 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
print()

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, '是质数')


print('break'.center(100, '-'))
# break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')


print('continue'.center(100, '-'))
# continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')


print('pass'.center(100, '-'))
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，防止语法错误
# while True:
#     pass  # 等待键盘中断 (Ctrl+C)


# 最小的类:
class MyEmptyClass:
    pass


for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")