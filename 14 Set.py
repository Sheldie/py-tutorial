# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print()
# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合。
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

# 两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    # 集合a中包含而集合b中不包含的元素
print(a | b)    # 集合a或b中包含的所有元素
print(a & b)    # 集合a和b中都包含了的元素
print(a ^ b)    # 不同时包含于a和b的元素

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


print('add() / update()'.center(100, '-'))
# add()：用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
# set.add(elmnt)
# elmnt -- 必需，要添加的元素。
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.add("apple")
print(fruits)

# update()：用于修改当前集合，可以添加新的元素或集合到当前集合中
# 如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
# set.update(set)
# set -- 必需，可以是元素或集合
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.update(y)
print(x)


print('clear()'.center(100, '-'))
# clear()：用于移除集合中的所有元素。
# set.clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)


print('copy()'.center(100, '-'))
# copy()：用于拷贝一个集合。
# set.copy()
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
fruits.add("orange")
print(x)


print('difference() / difference_update()'.center(100, '-'))
# difference()：用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。
# set.difference(set)
# set -- 必需，用于计算差集的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# difference_update()：用于移除两个集合中都存在的元素。
# difference()返回一个移除相同元素的新集合
# 而 difference_update()是直接在原来的集合中移除元素，没有返回值。
# set.difference_update(set)
# set -- 必需，用于计算差集的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


print('intersection() / intersection_update()'.center(100, '-'))
# intersection()：用于返回两个或更多集合中都包含的元素，即交集。
# set.intersection(set1, set2 ... etc)
# set1 -- 必需，要查找相同元素的集合
# set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.intersection(y)
print(z)
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)

# intersection_update()：用于获取两个或更多集合中都重叠的元素，即计算交集。
# intersection()是返回一个新的集合
# 而 intersection_update()是在原始的集合上移除不重叠的元素。
# set.intersection_update(set1, set2 ... etc)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.intersection_update(y)
print(x)
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)


print('isdisjoint()'.center(100, '-'))
# isdisjoint()：用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# set.isdisjoint(set)
# set -- 必需，要比较的集合
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "facebook"}
z = x.isdisjoint(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.isdisjoint(y)
print(z)


print('issubset() / issuperset()'.center(100, '-'))
# issubset()：用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
# set.issubset(set)
# set -- 必需，要比查找的集合
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

# issuperset()：用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
# set.issuperset(set)
# set -- 必需，要比查找的集合
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


print('len()'.center(100, '-'))
# 计算集合元素个数
# len(s)
thisset = {"Google", "Runoob", "Taobao"}
print(len(thisset))


print('x in set'.center(100, '-'))
# 判断元素是否在集合中存在
# x in set
thisset = {"Google", "Runoob", "Taobao"}
print("Runoob" in thisset)
print("Facebook" in thisset)


print('pop() / remove() / discard()'.center(100, '-'))
# pop()：用于随机移除一个元素。
# set.pop()
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(fruits)
print(x)
# 多次执行测试结果都不一样。
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

# remove()：用于移除集合中的指定元素。
# s.remove( x )
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
thisset = {"Google", "Runoob", "Taobao"}
thisset.remove("Taobao")
print(thisset)
# thisset.remove("Facebook")   # 不存在会发生错误

# s.discard( x )
# 移除集合中的元素，且如果元素不存在，不会发生错误
thisset = {"Google", "Runoob", "Taobao"}
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)


print('symmetric_difference() / symmetric_difference_update()'.center(100, '-'))
# symmetric_difference()：返回两个集合中不重复的元素集合，但会移除两个集合中都存在的元素。
# set.symmetric_difference(set)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.symmetric_difference(y)
print(z)

# symmetric_difference_update()：移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# set.symmetric_difference_update(set)
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.symmetric_difference_update(y)
print(x)


print('union()'.center(100, '-'))
# union()：返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
# set.union(set1, set2...)
# set1 -- 必需，合并的目标集合
# set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)
