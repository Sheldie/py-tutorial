# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 列表

print()
print('定义'.center(100, '-'))
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)
print(li[1])

print()
print('索引'.center(100, '-'))
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

print()
print('增加元素'.center(100, '-'))
li.append("new")
print(li)
li.insert(2, "new")
print(li)
li.extend(["two", "elements"])
print(li)

print()
print('搜索'.center(100, '-'))
print(li.index("example"))
print(li.index("new"))
# print(li.index("c"))
print("c" in li)

print()
print('删除'.center(100, '-'))
li.remove("z")
print(li)
li.remove("new")    # 删除首次出现的一个值
print(li)
# li.remove("c")
print(li.pop())
print(li)

print()
print('运算符'.center(100, '-'))
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)
li += ['two']
print(li)
li = [1, 2] * 3
print(li)

print()
print('使用join链接list成为字符串'.center(100, '-'))
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
ls = ["%s=%s" % (k, v) for k, v in params.items()]
s = ";".join(ls)
print(ls)
print(s)

print()
print('分割字符串'.center(100, '-'))
print(s.split(";"))
print(s.split(";", 1))
# split 接受一个可选的第二个参数, 它是要分割的次数。

print()
print('映射解析'.center(100, '-'))
li = [1, 9, 8, 4]
print([elem*2 for elem in li])

print()
print('dictionary 中的解析'.center(100, '-'))
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])

print()
print('list 过滤'.center(100, '-'))
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])

