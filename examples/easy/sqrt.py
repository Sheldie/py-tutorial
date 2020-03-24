# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import cmath

# 只适用于正数
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print('%0.3f 的平方根为 %0.3f' % (num, num_sqrt))

# 计算实数和复数平方根
# 导入复数数学模块
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
