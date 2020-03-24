# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 用户输入数字

num = float(input("输入一个数字: "))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

# 内嵌 if 语句
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")


num = int(input("输入一个数字: "))
if (num % 2) == 0:
   print("{0} 是偶数".format(num))
else:
   print("{0} 是奇数".format(num))

# num = eval(input('Number:\n'))
print('{} is '.format(num) + ('even number.' if num % 2 == 0 else 'odd number.'))


year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))
