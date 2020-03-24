# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import math
# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    # 找到其平方根（ √ ），减少算法时间
    square_num = math.floor(num ** 0.5)
    # 查找其因子
    for i in range(2, (square_num+1)):
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "x", num // i, "=", num)
            break
    else:
        print(num, "是质数")
        # 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "既不是质数，也不是合数")


print()
# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
print("素数结果如下：")
for num in range(lower, upper + 1):
    # 找到其平方根（ √ ），减少算法时间
    square_num = math.floor(num ** 0.5)
    # 素数大于 1
    if num > 1:
        for i in range(2, (square_num + 1)):
            if (num % i) == 0:
                break
        else:
            print(num)
