# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

from collections import Counter

print('len()'.center(100, '-'))
# len()：返回列表元素个数
# len(list)
# list -- 要计算元素个数的列表
list1 = ['Google', 'Runoob', 'Taobao']
print(len(list1))
list2 = list(range(5))  # 创建一个 0-4 的列表
print(len(list2))

print('max() / min()'.center(100, '-'))
# max()：返回列表元素中的最大值。
# max(list)
# list -- 要返回最大值的列表。
list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print("list1 最大元素值 : ", max(list1))
print("list2 最大元素值 : ", max(list2))
# 当元素全部为数字类型时，直接根据值的大小比较
# 当元素全部为字符串类型(string)时，则比较的是每个字符串元素的第一个字符的 ASCII 的大小
# 如果列表或者元组中的元素为数字类型和字符串类型混杂时，则无法比较。
print("list1 最小元素值 : ", min(list1))
print("list2 最小元素值 : ", min(list2))

print('list()'.center(100, '-'))
# list()：用于将元组或字符串转换为列表。
# 注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
# list(seq)
# seq -- 要转换为列表的元组或字符串。
aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print("列表元素 : ", list1)
str = "Hello World"
list2 = list(str)
print("列表元素 : ", list2)

print('append()'.center(100, '-'))
# append()：用于在列表末尾添加新的对象。
# list.append(obj)
# obj -- 添加到列表末尾的对象。
list = ['Google', 'Runoob', 'Taobao']
list.append('Baidu')
print(list)
list.append([1, 2, 3])
print(list)
list.extend([1, 2, 3])
print(list)
# 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。
# append() 方法向列表的尾部添加一个新的元素。
# 列表是以类的形式实现的。“创建”列表实际上是将一个类实例化。因此，列表有多种方法可以操作。
# extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。


print('count() / Counter'.center(100, '-'))
# count()：用于统计某个元素在列表中出现的次数。
# list.count(obj)
# obj -- 列表中统计的对象
aList = [123, 'Google', 'Runoob', 'Taobao', 123];
print("123 元素个数 : ", aList.count(123))
print("Runoob 元素个数 : ", aList.count('Runoob'))

# 统计字符出现的个数或列表内出现的元素次数等也可以用 Counter。
# 一个 Counter 是一个 dict 的子类，用于计数可哈希对象。
c = Counter('sadasfas')
print(c)
a = ['su', 'bu', 'sum', 'bu', 'sum', 'bu']
c = Counter(a)
print(c)
c.update('sadasfas')  # 添加
print(c)

print('extend()'.center(100, '-'))
# extend()：用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# list.extend(seq)
# seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
list = ['Google', 'Runoob', 'Taobao']
list.extend([1, 2, 3])
print(list)

print('index()'.center(100, '-'))
# index()：用于从列表中找出某个值第一个匹配项的索引位置。
# list.index(x[, start[, end]])
# x-- 查找的对象。
# start-- 可选，查找的起始位置。
# end-- 可选，查找的结束位置。
list1 = ['Google', 'Runoob', 'Taobao']
print('Runoob 索引值为', list1.index('Runoob'))
print('Taobao 索引值为', list1.index('Taobao'))
list2 = ['Google', 'Runoob', 'Taobao', 'Facebook', 'QQ']
print('Runoob 索引值为', list2.index('Runoob', 1))

print('insert()'.center(100, '-'))
# insert()：用于将指定对象插入列表的指定位置。
# list.insert(index, obj)
# index -- 对象obj需要插入的索引位置。
# obj -- 要插入列表中的对象。
list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print('列表插入元素后为 : ', list1)

# 对于层叠列表，如果增加的是列表中的一个元素（子列表），则新增的元素初始只作为原元素的一个镜像
# 这时候如果修改原元素（子列表）中的一个子元素，则新增元素同样变化，修改新元素中的子元素也是如此。
a = [[0, 1], [1, 2], [2, 3]]
a.insert(2, a[1])
a.append(a[3])
print(a)
a[1][1] = 0
a[4][1] = 4
print(a)
# 如果想只修改其中一个元素（子列表），必须把该子列表完整定义一遍，如在上述代码后增加。
a[1] = [1, 1]
print(a)
# 此后再修改子元素，不会发生联动
a[1][1] = 5
print(a)

print('pop()'.center(100, '-'))
# pop()：用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# list.pop([index=-1])
# index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
list1 = ['Google', 'Runoob', 'Taobao', 'Tencent']
list1.pop(1)
print("列表现在为 : ", list1)
list1.pop()
print("列表现在为 : ", list1)

print('remove()'.center(100, '-'))
# remove()：用于移除列表中某个值的第一个匹配项。
# list.remove(obj)
# obj -- 列表中要移除的对象。
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print("列表现在为 : ", list1)
list1.remove('Baidu')
print("列表现在为 : ", list1)

print('reverse()'.center(100, '-'))
# reverse()：用于反向列表中元素。
# list.reverse()
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print("列表反转后: ", list1)

print('sort()'.center(100, '-'))
# sort()：用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
# list.sort( key=None, reverse=False)
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# sort 方法不适合不同类型元素的比较。
# 在汉字、英文单词都存在的情况下,会优先对英文字母排序,然后再是汉字的首字母排序
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print("List : ", aList)
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('降序输出:', vowels)


def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key=takeSecond)
print('排序列表：', random)

# 根据列表中元素的多个属性进行排序
list = [["1","c++","demo"],
       ["1","c","test"],
       ["2","java",""],
       ["8","golang","google"],
       ["4","python","gil"],
       ["5","swift","apple"]
]
list.sort(key=lambda ele:ele[0])    # 根据第1个元素排序
print(list)
list.sort(key=lambda ele:ele[1])    # 根据第2个元素排序
print(list)
list.sort(key=lambda ele:ele[1]+ele[0])     # 先根据第2个元素排序，再根据第1个元素排序
print(list)


def two_d_list_sort(sort_index="0,1,2"):  # 动态的根据传入的元素索引进行排序
    list = [["1", "c++", "demo"],
            ["1", "c", "test"],
            ["2", "java", ""],
            ["8", "golang", "google"],
            ["4", "python", "gil"],
            ["5", "swift", "apple"]
            ]
    key_set = ""
    for item in sort_index.split(","):
        key_set += "ele[" + item + "]+"
    key_set = key_set.rstrip("+")
    list.sort(key=lambda ele: eval(key_set))
    print("排序索引:", sort_index, list)


if __name__ == "__main__":
    two_d_list_sort("0")
    two_d_list_sort("1")
    two_d_list_sort("2")
    two_d_list_sort("1,0")


print('clear()'.center(100, '-'))
# clear()：用于清空列表，类似于 del a[:]。
# list.clear()
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print("列表清空后 : ", list1)
# 通过 clear() 方法，remove() 方法，pop() 方法，append() 方法等改变列表的，相应的已经赋值给其它变量的列表也会被改变。


print('copy()'.center(100, '-'))
# copy()：用于复制列表，类似于 a[:]。
# list.copy()
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print("list2 列表: ", list2)
