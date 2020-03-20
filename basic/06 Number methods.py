# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import math
import random
import string

print('abs()'.center(100, '-'))
# abs()：返回数字的绝对值。
# abs(x)
# x -- 数值表达式，可以是整数，浮点数，复数。
# fabs() 函数只适用于 float 和 integer 类型，而 abs() 也适用于复数。
print("abs(-40) : ", abs(-40))
print("abs(100.10) : ", abs(100.10))
# 输入是复数时， 返回这个复数的模。
v = complex(3, 4)
print(abs(v))
print("math.fabs(-45.17) : ", math.fabs(-45.17))
# abs() 是内置函数。 fabs() 函数在 math 模块中定义。
# fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中。


print('ceil(x)'.center(100, '-'))
# ceil(x)：返回一个大于或等于 x 的的最小整数。
# math.ceil( x )
print("math.ceil(-45.17) : ", math.ceil(-45.17))
print("math.ceil(100.12) : ", math.ceil(100.12))
print("math.ceil(100.72) : ", math.ceil(100.72))
print("math.ceil(math.pi) : ", math.ceil(math.pi))
print("math.ceil(math.pi) : ", math.ceil(math.e))


print('cmp()'.center(100, '-'))
# 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
x = 3
y = 5
print((x > y) - (x < y))
x = 5
y = 3
print((x > y) - (x < y))
x = 4
y = 4
print((x > y) - (x < y))


print('exp()'.center(100, '-'))
# exp()：返回x的指数，e的x次方。
# math.exp( x )
# x -- 数值表达式。
print("math.exp(-45.17) : ", math.exp(-45.17))
print("math.exp(100.12) : ", math.exp(100.12))
print("math.exp(100.72) : ", math.exp(100.72))
print("math.exp(math.pi) : ", math.exp(math.pi))


print('floor(x)'.center(100, '-'))
# floor(x)：返回数字的下舍整数，小于或等于 x。
# math.floor( x )
print("math.floor(-45.17) : ", math.floor(-45.17))
print("math.floor(100.12) : ", math.floor(100.12))
print("math.floor(100.72) : ", math.floor(100.72))
print("math.floor(math.pi) : ", math.floor(math.pi))


print('log()'.center(100, '-'))
# log()：返回x的自然对数，x > 0。
# math.log( x )
print("math.log(100.12) : ", math.log(100.12))
print("math.log(100.72) : ", math.log(100.72))
print("math.log(math.pi) : ", math.log(math.pi))
print("math.log(100, 10) : ", math.log(100, 10))


print('log10()'.center(100, '-'))
# log10()：返回以10为基数的x对数，x>0。
# math.log10( x )
print("math.log10(100.12) : ", math.log10(100.12))
print("math.log10(100.72) : ", math.log10(100.72))
print("math.log10(119) : ", math.log10(119))
print("math.log10(math.pi) : ", math.log10(math.pi))


print('min() / max()'.center(100, '-'))
# min()：返回给定参数的最小值，参数可以为序列。
# max()：返回给定参数的最大值，参数可以为序列。
# min( x, y, z, .... )
# max( x, y, z, .... )
print("min(80, 100, 1000) : ", min(80, 100, 1000))
print("min(-20, 100, 400) : ", min(-20, 100, 400))
print("min(-80, -20, -10) : ", min(-80, -20, -10))
print("min(0, 100, -400) : ", min(0, 100, -400))
print("max(0, 100, -400) : ", max(0, 100, -400))
list = (0, 100, -400)
print("min(list) : ", min(list))
print("max(list) : ", max(list))


print('modf()'.center(100, '-'))
# modf()：返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# math.modf( x )
print("math.modf(100.12) : ", math.modf(100.12))
print("math.modf(100.72) : ", math.modf(100.72))
print("math.modf(119) : ", math.modf(119))
print("math.modf(math.pi) : ", math.modf(math.pi))


print('pow()'.center(100, '-'))
# pow()：返回 xy（x的y次方） 的值。
# math.pow( x, y )
# pow(x, y[, z])
# 函数是计算x的y次方，如果z存在则再对结果进行取模，其结果等效于pow(x,y) %z
# pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。
print("math.pow(100, 2) : ", math.pow(100, 2))
print("pow(100, 2) : ", pow(100, 2))
print("pow(100, 2, 7) : ", pow(100, 2, 7))
print("math.pow(100, -2) : ", math.pow(100, -2))
print("math.pow(2, 4) : ", math.pow(2, 4))
print("math.pow(3, 0) : ", math.pow(3, 0))


print('round()'.center(100, '-'))
# round()：返回返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。
# 保留值将保留到离上一位更近的一端。
# 精度要求高的，不建议使用该函数。
print("round(70.23456) : ", round(70.23456))
print("round(56.659,1) : ", round(56.659, 1))
print("round(80.264, 2) : ", round(80.264, 2))
print("round(100.000056, 3) : ", round(100.000056, 3))
print("round(-100.000056, 3) : ", round(-100.000056, 3))


print('sqrt()'.center(100, '-'))
# sqrt()：返回数字x的平方根。
# math.sqrt( x )
print("math.sqrt(100) : ", math.sqrt(100))
print("math.sqrt(7) : ", math.sqrt(7))
print("math.sqrt(math.pi) : ", math.sqrt(math.pi))

print("101-200之间的素数是：", end="")
for i in range(100, 201):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0: break
    else:
        print("", i, end="")
else:
    print()

x = 4
a = math.sqrt(x)
print(int(a) == a)


# 随机数函数
print('choice()'.center(100, '-'))
# choice()：返回一个列表，元组或字符串的随机项。
# random.choice(seq)
print("从 range(100) 返回一个随机数 : ", random.choice(range(100)))
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

# 创建随机密码
# a = int(input('请输入要求的密码长度'))
a = 8
b = string.digits + string.ascii_letters + string.punctuation   # 构建密码池
password = ""   # 命名一个字符串
for i in range(0, a):    # for loop 指定重复次数
    password = password + random.choice(b)  # 从密码池中随机挑选内容构建密码
print(password)     # 输出密码


print('randrange()'.center(100, '-'))
# randrange()：返回指定递增基数集合中的一个随机数，基数默认值为1。
# random.randrange ([start,] stop [,step])
# start -- 指定范围内的开始值，包含在范围内
# stop -- 指定范围内的结束值，不包含在范围内
# step -- 指定递增基数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))    # 从 1-100 中选取一个奇数
print("randrange(100) : ", random.randrange(100))   # 从 0-99 选取一个随机数
print("randrange(1,100, 3) : ", random.randrange(1,100, 3))   # 从0-100中随机选取一个能被3整除后余1的数


print('seed()'.center(100, '-'))
# seed()：改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
# random.seed ( [x] )
# x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# 调用 random.random() 生成随机数时，每一次生成的数都是随机的。
# 但是预先使用 random.seed(x) 设定好种子之后，使用 random() 生成的随机数将会是同一个。
random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())


print('uniform()'.center(100, '-'))
# uniform()：将随机生成下一个实数，它在 [x,y] 范围内。
# random.uniform(x, y)
print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))


# 三角函数
print('acos()'.center(100, '-'))
# acos()：返回x的反余弦弧度值。
# math.acos(x)
# x -- -1到1之间的数值。如果x是大于1，会产生一个错误。
print("acos(0.64) : ",  math.acos(0.64))
print("acos(0) : ",  math.acos(0))
print("acos(-1) : ",  math.acos(-1))
print("acos(1) : ",  math.acos(1))


print('asin()'.center(100, '-'))
# asin()：返回x的反正弦弧度值。
# math.asin(x)
# x -- -1到1之间的数值。如果x是大于1，会产生一个错误。
print("asin(0.64) : ",  math.asin(0.64))
print("asin(0) : ",  math.asin(0))
print("asin(-1) : ",  math.asin(-1))
print("asin(1) : ",  math.asin(1))


print('atan()'.center(100, '-'))
# atan()：返回x的反正切弧度值。
# math.atan(x)
print("atan(0.64) : ",  math.atan(0.64))
print("atan(0) : ",  math.atan(0))
print("atan(10) : ",  math.atan(10))
print("atan(-1) : ",  math.atan(-1))
print("atan(1) : ",  math.atan(1))


print('atan2()'.center(100, '-'))
# atan2()：返回给定的 X 及 Y 坐标值的反正切值。
# math.atan2(y, x)
print("atan2(-0.50,-0.50) : ",  math.atan2(-0.50, -0.50))
print("atan2(0.50,0.50) : ",  math.atan2(0.50, 0.50))
print("atan2(5,5) : ",  math.atan2(5, 5))
print("atan2(-10,10) : ",  math.atan2(-10, 10))
print("atan2(10,20) : ",  math.atan2(10, 20))


print('cos()'.center(100, '-'))
# cos()：返回x的弧度的余弦值
# math.cos(x)
print("cos(3) : ",  math.cos(3))
print("cos(-3) : ",  math.cos(-3))
print("cos(0) : ",  math.cos(0))
print("cos(math.pi) : ",  math.cos(math.pi))
print("cos(2*math.pi) : ",  math.cos(2 * math.pi))


print('hypot()'.center(100, '-'))
# hypot()：返回欧几里德范数 sqrt(x*x + y*y)
# math.hypot(x, y)
print("hypot(3, 2) : ",  math.hypot(3, 2))
print("hypot(-3, 3) : ",  math.hypot(-3, 3))
print("hypot(0, 2) : ",  math.hypot(0, 2))


print('sin()'.center(100, '-'))
# sin()：返回x弧度的正弦值
# math.sin(x)
print("sin(3) : ",  math.sin(3))
print("sin(-3) : ",  math.sin(-3))
print("sin(0) : ",  math.sin(0))
print("sin(math.pi) : ",  math.sin(math.pi))
print("sin(math.pi/2) : ",  math.sin(math.pi/2))


print('tan()'.center(100, '-'))
# tan()：返回 x 弧度的正切值
# math.tan(x)
print("(tan(3) : ",  math.tan(3))
print("tan(-3) : ",  math.tan(-3))
print("tan(0) : ",  math.tan(0))
print("tan(math.pi) : ",  math.tan(math.pi))
print("tan(math.pi/2) : ",  math.tan(math.pi/2))
print("tan(math.pi/4) : ",  math.tan(math.pi/4))


print('degrees()'.center(100, '-'))
# degrees()：将弧度转换为角度
# math.degrees(x)
print("degrees(3) : ",  math.degrees(3))
print("degrees(-3) : ",  math.degrees(-3))
print("degrees(0) : ",  math.degrees(0))
print("degrees(math.pi) : ",  math.degrees(math.pi))
print("degrees(math.pi/2) : ",  math.degrees(math.pi/2))
print("degrees(math.pi/4) : ",  math.degrees(math.pi/4))


print('radians()'.center(100, '-'))
# radians()：将角度转换为弧度
# math.radians(x)
print("radians(3) : ",  math.radians(3))
print("radians(-3) : ",  math.radians(-3))
print("radians(0) : ",  math.radians(0))
print("radians(math.pi) : ",  math.radians(math.pi))
print("radians(math.pi/2) : ",  math.radians(math.pi/2))
print("radians(math.pi/4) : ",  math.radians(math.pi/4))


