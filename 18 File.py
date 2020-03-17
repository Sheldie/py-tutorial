# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# open()
# 用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

# 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。
# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
# open(file, mode='r')
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener:
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# b	二进制模式。
# +	打开一个文件进行更新(可读可写)。
# U	通用换行模式（Python 3 不支持）。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# 默认为文本模式，如果要以二进制模式打开，加上 b 。

print()
# file 对象
# file 对象使用 open 函数来创建

# 打开文件
# fo = open("runoob.txt", "wb")
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)
# 关闭文件
fo.close()


print()
# flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
# 一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
# fileObject.flush();
# fo = open("runoob.txt", "wb")
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)
# 刷新缓冲区
fo.flush()
# 关闭文件
fo.close()


print()
# fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。
# fileObject.fileno();
# fo = open("runoob.txt", "wb")
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)
fid = fo.fileno()
print("文件描述符为: ", fid)
fo.close()


print()
# isatty() 方法检测文件是否连接到一个终端设备，如果是返回 True，否则返回 False。
# fileObject.isatty();
# fo = open("runoob.txt", "wb")
fo = open("runoob.txt", "r+")
print("文件名为: ", fo.name)
ret = fo.isatty()
print("返回值 : ", ret)
fo.close()


print()
# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
# fileObject.read();
# size -- 从文件中读取的字节数。
# 返回从字符串中读取的字节。

# fo = open("runoob.txt", "r+")
# Traceback (most recent call last):
#   File "D:/Projects/py-tutorital/18 File.py", line 95, in <module>
#     line = fo.read(10)
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 8: illegal multibyte sequence

fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名为: ", fo.name)
line = fo.read(10)
print("读取的字符串: %s" % (line))
fo.close()


print()
# readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
# fileObject.readline();
# size -- 从文件中读取的字节数。
# 返回从字符串中读取的字节。
fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取第一行: ", line[0:-1])    # line[0:-1]去掉 "\n"
line = fo.readline(5)
print("读取的字符串为: ", line)
fo.close()


print()
# readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
# 如果碰到结束符 EOF 则返回空字符串。
# fileObject.readlines();
fo = open("runoob.txt", "r", encoding="utf-8")
print("文件名为: ", fo.name)
for line in fo.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    print("读取的数据为: %s" % line)
fo.close()


print()
# seek() 方法用于移动文件读取指针到指定位置。
# fileObject.seek(offset[, whence])
# offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
# whence：可选，默认值为 0。
# 给 offset 定义一个参数，表示要从哪个位置开始偏移；0 代表从文件开头开始算起，1 代表从当前位置开始算起，2 代表从文件末尾算起。
# 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1。
f = open('workfile.txt', 'wb+')
f.write(b'0123456789abcdef')
f.seek(5)      # 移动到文件的第六个字节
print(f.read(1))
f.seek(-3, 2)  # 移动到文件倒数第三个字节
print(f.read(1))

print()
# 循环读取文件的内容
fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取的数据为: %s" % line[0:-1])
# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print("读取的数据为: %s" % line[0:-1])
# 关闭文件
fo.close()


print()
# tell() 方法返回文件的当前位置，即文件指针当前位置。
# fileObject.tell()
fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名为: ", fo.name)
line = fo.readline()
print("读取的数据为: %s" % line[0:-1])
pos = fo.tell()
print("当前位置: %d" % pos)
fo.close()


print()
# truncate() 方法用于从文件的首行首字节开始截断，截断文件为 size 个字节，无 size 表示从当前位置截断；
# 截断之后 V 后面的所有字节被删除，其中 Windows 系统下的换行代表2个字节大小。
# fileObject.truncate( [ size ])
# size -- 可选，如果存在则文件截断为 size 字节。
fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名: ", fo.name)
line = fo.readline()
print("读取行: %s" % line)
fo.truncate()
lines = fo.readlines()
print("读取行: %s" % lines)
fo.close()


print()
# write() 方法用于向文件中写入指定字符串。
# 在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时在文件中是看不到写入的内容的
# 如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，
# 否则报错：TypeError: a bytes-like object is required, not 'str'。
# fileObject.write( [ str ])
# str -- 要写入文件的字符串。
# 返回的是写入的字符长度。
fo = open("runoob.txt", "r+", encoding="utf-8")
print("文件名: ", fo.name)
str = "6:www.runoob.com"
fo.seek(0, 2)
line = fo.write(str)
fo.seek(0, 0)
index = 0
for line in fo.readlines():
    index += 1
    line = line.strip()
    print("文件行号 %d - %s" % (index, line))
fo.close()


print()
# writelines() 方法用于向文件中写入一序列的字符串。
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 换行需要制定换行符 \n。
fo = open("test.txt", "w")
print("文件名为: ", fo.name)
seq = ["菜鸟教程 1\n", "菜鸟教程 2"]
fo.writelines(seq)
fo.close()

