# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# greatest common divisor
# 最大公约数

# least common multiple
# 最小公倍数


# 辗转相除
def find_GCD(x, y):
    find_GCD = y
    while (x % y) != 0:
        find_GCD = x % y
        x, y = y, find_GCD
    return find_GCD


def find_LCM(x, y):
    return int(x * y / find_GCD(x, y))


int1 = int(input('Input 1st integer: '))
int2 = int(input('Input 2nd integer: '))

print('The LCM of {} and {} is {}'.format(int1, int2, find_LCM(int1, int2)))
print('The GCD of {} and {} is {}'.format(int1, int2, find_GCD(int1, int2)))
