# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print('len() / str() / type()'.center(100, '-'))
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))
print(str(dict))
print(type(dict))


print('clear()'.center(100, '-'))
# clear()：用于删除字典内所有元素。
dict.clear()
dict = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dict))
dict.clear()
print("字典删除后长度 : %d" % len(dict))


print('copy()'.center(100, '-'))
# copy()：返回一个字典的浅复制
# dict.copy()
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print("新复制的字典为 : ", dict2)

print()
# 直接赋值和 copy 的区别
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)
# 输出结果
print(dict1)
print(dict2)
print(dict3)
# 实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的
# dict3 父对象进行了深拷贝，不会随 dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。


print('fromkeys()'.center(100, '-'))
# fromkeys()：用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
# dict.fromkeys(seq[, value])
# seq -- 字典键值列表。
# value -- 可选参数, 设置键序列（seq）对应的值，默认为 None。
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dict))
dict = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dict))


print('get()'.center(100, '-'))
# get()：返回指定键的值，如果值不在字典中返回默认值。
# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。
dict = {'Name': 'Runoob', 'Age': 27}
print("Age 值为 : %s" % dict.get('Age'))
print("Sex 值为 : %s" % dict.get('Sex', "NA"))


print('in / not in'.center(100, '-'))
# 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
# 而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
# key in dict
# key -- 要在字典中查找的键。
dict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if 'Age' in dict:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in

# 检测键 Age 是否存在
if 'Age' not in dict:
    print("键 Age 不存在")
else:
    print("键 Age 存在")


print('items()'.center(100, '-'))
# items()：以列表返回可遍历的(键, 值) 元组数组。
# dict.items()
dict = {'Name': 'Runoob', 'Age': 7}
print("Value : %s" % dict.items())

# 遍历
dict = {'Name': 'Runoob', 'Age': 7}
for i, j in dict.items():
    print(i, ":\t", j)

# 将字典的 key 和 value 组成一个新的列表
d = {1: "a", 2: "b", 3: "c"}
result = []
for k, v in d.items():
    result.append(k)
    result.append(v)
print(result)


print('keys()'.center(100, '-'))
# keys()：返回一个可迭代对象，可以使用 list() 来转换为列表。
# dict.keys()
dict = {'Name': 'Runoob', 'Age': 7}
print(dict.keys())
print(list(dict.keys()))   # 转换为列表


print('setdefault()'.center(100, '-'))
# setdefault() 方法和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
# dict.setdefault(key, default=None)
# key -- 查找的键值。
# default -- 键不存在时，设置的默认键值。
dict = {'Name': 'Runoob', 'Age': 7}
print("Age 键的值为 : %s" % dict.setdefault('Age', None))
print("Sex 键的值为 : %s" % dict.setdefault('Sex', None))
print("新字典为：", dict)


print('update()'.center(100, '-'))
# update()：把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
# dict.update(dict2)
# dict2 -- 添加到指定字典dict里的字典。
dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female'}
dict.update(dict2)  # 合并字典
print("更新字典 dict : ", dict)
# 如果键值有重复，则 dict2 的内容更新替换到 dict 中

# 排序
d1 = {}
for k in sorted(dict.keys()):
    d = {k: dict[k]}
    d1.update(d)
print(d1)

# 使用 **，函数将参数以字典的形式导入
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = {**dict1, **dict2}  # *表示数据类型为tuple, **表示dict
print(dict3)


print('values()'.center(100, '-'))
# values()：返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print(dict.values())
print("字典所有值为 : ", list(dict.values()))


print('pop()'.center(100, '-'))
# pop()：删除字典给定键key所对应的值，返回值为被删除的值。key值必须给出。否则返回default值。
# key: 要删除的键值
# default: 如果没有 key，返回 default 值
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.pop('name')
print(pop_obj)
print(site)

# 批量删除
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
# 输出原始的字典
print("字典移除前 : " + str(test_dict))
# 使用 pop 批量移除
new_dict = {key: val for key, val in test_dict.items() if val > 2}
print("字典移除后 : " + str(new_dict))


print('popitem()'.center(100, '-'))
# popitem()：随机返回并删除字典中的最后一对键和值。
# 如果字典已经为空，却调用了此方法，就报出KeyError异常。
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj = site.popitem()
print(pop_obj)
print(site)


print('lambda()'.center(100, '-'))
# 按键(key)或值(value)对字典进行排序
# 声明字典
key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print("按值(value)排序:")
print(sorted(key_value.items(), key=lambda kv: kv[1]))
print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))
print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))


# sorted(key_value) 返回一个迭代器
# 字典按键排序
for i in sorted(key_value):
    print((i, key_value[i]), end=" ")


print()
# 字典列表排序
lis = [{"name": "Taobao", "age": 100},
       {"name": "Runoob", "age": 7},
       {"name": "Google", "age": 100},
       {"name": "Wiki", "age": 200}]

# 通过 age 升序排序
print("列表通过 age 升序排序: ")
print(sorted(lis, key=lambda i: i['age']))
print("\r")
# 先按 age 排序，再按 name 排序
print("列表通过 age 和 name 排序: ")
print(sorted(lis, key=lambda i: (i['age'], i['name'])))
print("\r")
# 按 age 降序排序
print("列表通过 age 降序排序: ")
print(sorted(lis, key=lambda i: i['age'], reverse=True))
print()


# 计算字典值之和
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum += myDict[i]

    return sum


dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))