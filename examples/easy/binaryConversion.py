# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 进制转换

# 获取用户输入十进制数
# dec = int(input("输入数字："))
dec = 13

print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

print()
print("八进制转二进制:", bin(0o15))

print()
print("十六进制转二进制:", bin(0xd))

print()
print("二进制转八进制:", oct(0b1101))

print()
print("二进制转十进制:", int('1101', 2))

print()
print("八进制转十进制:", int('0o226', 8))

print()
print("十六进制转十进制:", int('0x96', 16))


