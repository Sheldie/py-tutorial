# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print()
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"   # 不需要括号也可以
print(type(tup3))


tup1 = (50)
print(type(tup1))   # 不加逗号，类型为整型
tup1 = (50,)
print(type(tup1))   # 加上逗号，类型为元组


print()
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])


print()
# 元组中的元素值是不允许修改的，但可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)


print()
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
print(tup)
del tup
print("删除后的元组 tup : ")
# print(tup)
# NameError: name 'tup' is not defined


# 元组运算符
# Python 表达式	                    结果	                                描述
# len((1, 2, 3))	                3	                                    计算元素个数
# (1, 2, 3) + (4, 5, 6)	            (1, 2, 3, 4, 5, 6)	                    连接
# ('Hi!',) * 4	                    ('Hi!', 'Hi!', 'Hi!', 'Hi!')	        复制
# 3 in (1, 2, 3)	                True	                                元素是否存在
# for x in (1, 2, 3): print (x,)	1 2 3	                                迭代


print()
# 元组也是一个序列，可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
L = ('Google', 'Taobao', 'Runoob')
print(L[2])
print(L[-2])
print(L[1:])

print('Methods'.center(100, '-'))
tuple1 = ('Google', 'Runoob', 'Taobao')
print(len(tuple1))

tuple2 = ('5', '4', '8')
print(max(tuple2))
print(min(tuple2))

list1 = ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)


print('Tips'.center(100, '-'))
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
# 从实例可以看出，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。
tup = ('r', 'u', 'n', 'o', 'o', 'b')
# tup[0] = 'g'     # 不支持修改元素
print(id(tup))     # 查看内存地址
tup = (1, 2, 3)
print(id(tup))
