# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


def search(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


# 在数组 arr 中查找字符 D
arr = ['A', 'B', 'C', 'D', 'E'];
x = 'B'
n = len(arr)
result = search(arr, n, x)
if result == -1:
    print("元素不在数组中")
else:
    print("元素在数组中的索引为", result)
