# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

import sys
import inspect

# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")


# list = [1, 2, 3, 4]
# it = iter(list)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


print()
print('Create an iterator'.center(100, '-'))
# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 面向对象编程：类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print('StopIteration'.center(100, '-'))
# StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x, end=" ")
print()


print('Generator'.center(100, '-'))
# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息
# 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。

def fab(max):   # 生成器函数 - 斐波那契
    n, a, b = 0, 0, 1
    while n < max:
        yield b     # 使用 yield
        # print b
        a, b = b, a + b     # 先计算 = 号右边的值，暂时不考虑左边的值。可以得到：b=1；a+b=1，再将右边的值赋予给左边的值，所以a，b都是1。
        n += 1


for n in fab(5):
    print(n)


# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数
# Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行函数，而是返回一个 iterable 对象！
# 在 for 循环执行时，每次循环都会执行 fibonacci 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值
# 下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，函数继续执行，直到再次遇到 yield。

# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码
# 直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。

# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力
# 比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰


print()
# 判断一个函数是否是一个特殊的 generator 函数
print(inspect.isgeneratorfunction(fab))
