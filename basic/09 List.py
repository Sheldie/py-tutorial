# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。


# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 列表的数据项不需要具有相同的类型
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
print('创建与访问'.center(100, '-'))
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = list(range(5))
list5 = list(range(2, 5))
print("list1[0]: ", list1[0])
print("list1[-2]: ", list1[-2])     # 从右侧开始读取倒数第二个元素: count from the right
print("list1[1:]: ", list1[1:])     # 输出从第二个元素开始后的所有元素
print("list2[1:5]: ", list2[1:4])   # 左闭右开
print("list4: ", list4)
print("list5: ", list5)


print('更新与删除'.center(100, '-'))
list = ['Google', 'Runoob', 1997, 2000]
print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)
# append() / remove()

print('列表脚本操作符'.center(100, '-'))
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
print(len([1, 2, 3]))   # 长度
print([1, 2, 3] + [4, 5, 6])    # 组合
print(['Hi!'] * 4)  # 重复
print(3 in [1, 2, 3])   # 元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")   # 迭代
print()


print('列表截取与拼接'.center(100, '-'))
L = ['Google', 'Runoob', 'Taobao']
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)
print(squares[2])
print(squares[-2])
print(squares[3:])
print(squares[4:7])


print('列表嵌套'.center(100, '-'))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])