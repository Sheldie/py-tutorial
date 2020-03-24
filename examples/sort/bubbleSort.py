# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        flag = True
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i])
