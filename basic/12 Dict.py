# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
# d = {key1 : value1, key2 : value2 }

print()
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# print("dict['Alice']: ", dict['Alice'])
# Traceback (most recent call last):
#   File "D:/Projects/py-tutorital/12 Dict.py", line 19, in <module>
#     print("dict['Alice']: ", dict['Alice'])
# KeyError: 'Alice'

print('CRUD'.center(100, '-'))
dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
print(dict)

del dict['Name']    # 删除键 'Name'
print(dict)
dict.clear()        # 清空字典
del dict            # 删除字典


print('Tips'.center(100, '-'))
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print(dict)

# 键必须不可变，所以可以用数字、字符串或元组充当，而用列表就不行
# dict = {['Name']: 'Runoob', 'Age': 7}
# print("dict['Name']: ", dict['Name'])
# Traceback (most recent call last):
#   File "D:/Projects/py-tutorital/12 Dict.py", line 43, in <module>
#     dict = {['Name']: 'Runoob', 'Age': 7}
# TypeError: unhashable type: 'list'
