# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import keyword

print('keyword'.center(100, '-'))
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


print('Single line & multiple lines'.center(100, '-'))
print('hello'); print('hello again');
test_num = 1 + \
            2 + \
                3
print(test_num)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)
