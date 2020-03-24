# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


def fibo(nterms):
    # 第一和第二项
    n1 = 0
    n2 = 1
    count = 2

    # 判断输入的值是否合法
    if nterms <= 0:
        print("请输入一个正整数。")
    elif nterms == 1:
        print("斐波那契数列：")
        print(n1)
    else:
        print("斐波那契数列：")
        print(n1, n2, end=" ")
        while count < nterms:
            nth = n1 + n2
            print(nth, end=" ")
            # 更新值
            n1 = n2
            n2 = nth
            count += 1


def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


if __name__ == '__main__':
    # 获取用户输入
    nterms = int(input("您要输出几项? "))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        for i in range(nterms):
            print(recur_fibo(i), end=" ")

    print()
    fibo(nterms)
