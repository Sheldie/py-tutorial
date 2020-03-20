# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

print('capitalize()'.center(100, '-'))
# capitalize()：将字符串的第一个字母变成大写,其他字母变小写。
# str.capitalize()
str = 'hello world!'
print(str.capitalize())


print('center()'.center(100, '-'))
# center()：返回一个指定宽度 width 居中的字符串，fillchar 为填充的单个字符，默认为空格。
# 如果 width 小于字符串宽度直接返回字符串，不会截断
# str.center(width[, fillchar])
# width -- 字符串的总宽度。
# fillchar -- 填充字符。
str = 'hello world!'
print("str.center(40, '*') : ", str.center(40, '*'))


print('count()'.center(100, '-'))
# count()：用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# str.count(sub, start=0, end=len(string))
# sub -- 搜索的子字符串
# start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
# end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
runoob = 'www.runoob.com'
print("str.count('o') : ", runoob.count('o'))
sub = 'run'
print("str.count('run', 0, 10) : ", runoob.count(sub, 0, 10))


print('encode() / decode()'.center(100, '-'))
# encode() 方法以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
# str.encode(encoding='UTF-8',errors='strict')

# decode()：以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
# bytes.decode(encoding="utf-8", errors="strict")

# encoding -- 要使用的编码，如"UTF-8"。
# errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。
# 其他可能的值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))


print('endswith()'.center(100, '-'))
# endswith()：判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。
# str.endswith(suffix[, start[, end]])
# suffix -- 该参数可以是一个字符串或者是一个元素。
# start -- 字符串中的开始位置。
# end -- 字符串中的结束位置。
Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
print(Str.endswith(suffix, 10, 15))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))


print('expandtabs()'.center(100, '-'))
# expandtabs()：把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# str.expandtabs(tabsize=8)
# tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数
str = "this is\tstring example....wow!!!"
print("原始字符串: " + str)
print("替换 \\t 符号: " + str.expandtabs())
print("使用16个空格替换 \\t 符号: " + str.expandtabs(16))


print('find()'.center(100, '-'))
# find()：检测字符串中是否包含子字符串 str ，如果指定 beg（开始）和 end（结束）范围，则检查是否包含在指定范围内
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
# str.find(str, beg=0, end=len(string))
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。
str1 = "Runoob example....wow!!!exam!!"
str2 = "exam"
print(str1.find(str2))
print(str1.find(str2, 5))
print(str1.find(str2, 0, 5))
print(str1.find(str2, 10))


print('index()'.center(100, '-'))
# index()：检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
# 该方法与 python find()方法一样，只不过如果str不在string中会报一个异常。
# str.index(str, beg=0, end=len(string))
# str -- 指定检索的字符串
# beg -- 开始索引，默认为0。
# end -- 结束索引，默认为字符串的长度。
print(str1.index(str2))
print(str1.index(str2, 5))
# print(str1.index(str2, 10))     # 异常


print('isalnum()'.center(100, '-'))
# isalnum()：检测字符串是否由字母和数字组成。
# str.isalnum()
str = "runoob2016"  # 字符串没有空格，含空格返回False
print(str.isalnum())
str = "www.runoob.com"
print(str.isalnum())
str = "我爱python"    # 汉字也返回True
print(str.isalnum())


print('isalpha()'.center(100, '-'))
# isalpha()：检测字符串是否只由字母或文字组成。
# str.isalpha()
str = "runoob"
print(str.isalpha())
# 字母和中文文字
str = "runoob菜鸟教程"
print(str.isalpha())
str = "Runoob example....wow!!!"
print(str.isalpha())


print('isdecimal()'.center(100, '-'))
# isdecimal()：检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
# str.isdecimal()
str = "runoob2016"
print(str.isdecimal())
str = "23443434"
print(str.isdecimal())


print('isdigit()'.center(100, '-'))
# isdigit()：检测字符串是否只由数字组成。
# str.isdigit()
str = "123456"
print(str.isdigit())
str = "Runoob example....wow!!!"
print(str.isdigit())


print('islower()'.center(100, '-'))
# islower()：检测字符串是否由小写字母组成。
# str.islower()
str = "RUNOOB example....wow!!!"
print(str.islower())
str = "runoob example....wow!!!"
print(str.islower())


print('isnumeric()'.center(100, '-'))
# isnumeric()：检测字符串是否只由数字组成，数字可以是：Unicode 数字，全角数字（双字节），罗马数字，汉字数字。
# 指数类似 ² 与分数类似 ½ 也属于数字。
# str.isnumeric()
str = "runoob2016"
print(str.isnumeric())
str = "23443434"
print(str.isnumeric())
s = '\u00B23455'    # s = '²3455'
print(s.isnumeric())
s = '\u00BD'    # s = '½'
print(s.isnumeric())
a = "\u0030"    # unicode for 0
print(a.isnumeric())
b = "\u00B2"    # unicode for ²
print(b.isnumeric())
c = "10km2"
print(c.isnumeric())


print('isspace()'.center(100, '-'))
# isspace()：检测字符串是否只由空白字符组成。
# str.isspace()
str = "       "
print(str.isspace())
str = "Runoob example....wow!!!"
print(str.isspace())


print('istitle()'.center(100, '-'))
# istitle()：检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。（如果字符串是标题化的）
# str.istitle()
str = "This Is String Example...Wow!!!"
print(str.istitle())
str = "This is string example....wow!!!"
print(str.istitle())


print('isupper()'.center(100, '-'))
# isupper()：检测字符串中所有的字母是否都为大写。
# str.isupper()
str = "THIS IS STRING EXAMPLE....WOW!!!"
print(str.isupper())
str = "THIS is string example....wow!!!"
print(str.isupper())


print('join()'.center(100, '-'))
# join()：用于将序列中的元素以指定的字符连接生成一个新的字符串。
# str.join(sequence)
# sequence -- 要连接的元素序列
s1 = "-"
s2 = "*"
seq = ("r", "u", "n", "o", "o", "b")    # 字符串序列
print(s1.join(seq))
print(s2.join(seq))


print('len()'.center(100, '-'))
# len()：返回对象（字符、列表、元组等）长度或项目个数。
# len(s)
# s -- 对象
str = "runoob"
l = [1, 2, 3, 4, 5]
print(len(str))     # 字符串长度
print(len(l))       # 元组元素个数


print('ljust()'.center(100, '-'))
# ljust()：返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
# str.ljust(width[, fillchar])
# width -- 指定字符串长度。
# fillchar -- 填充字符，默认为空格。
str = "Runoob example....wow!!!"
print(str.ljust(50, '*'))
print(str.rjust(50, '*'))


print('lower()'.center(100, '-'))
# lower()：转换字符串中所有大写字符为小写。
# str.lower()
str = "Runoob EXAMPLE....WOW!!!"
print(str.lower())


print('lstrip()'.center(100, '-'))
# lstrip()：用于截掉字符串左边的空格或指定字符。
# str.lstrip([chars])
# chars --指定截取的字符。
str = "     this is string example....wow!!!     ";
print(str.lstrip())
str = "88888888this is string example....wow!!!8888888";
print(str.lstrip('8'))
print(str.rstrip('8'))


print('maketrans()'.center(100, '-'))
# maketrans()：用于创建字符映射的转换表
# 对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
# 注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans() 。
# str.maketrans(intab, outtab)
# intab -- 字符串中要替代的字符组成的字符串。
# outtab -- 相应的映射字符的字符串。
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab))

# 一个参数，该参数必须为字典
d = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 's':'6'}
trantab = str.maketrans(d)
st = 'just do it'
print(st.translate(trantab))

# 三个参数 x、y、z，第三个参数 z 必须是字符串，其字符将被映射为 None，即删除该字符
# 如果 z 中字符与 x 中字符重复，该重复的字符在最终结果中还是会被删除。也就是无论是否重复，只要有第三个参数 z，z 中的字符都会被删除。
x = 'abcdefs'
y = '1234567'
z = 'ot'
st = 'just do it'
trantab = str.maketrans(x, y, z)
print(st.translate(trantab))


print('max() / min()'.center(100, '-'))
# max()：返回字符串中最大的字母。
# 在有大小写的字符串中返回的是小写字母的最大值。
# max(str)
# str -- 字符串
str = "runoob"
print("最大字符: " + max(str))
str = "rUNOob"
print("最大字符: " + max(str))

# min()：返回字符串中最小的字母。
# min(str)
# str -- 字符串
str = "runoob"
print("最小字符: " + min(str))


print('replace()'.center(100, '-'))
# replace()：把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# str.replace(old, new[, max])
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串
# max -- 可选字符串, 替换不超过 max 次
str = "www.w3cschool.cc"
print("菜鸟教程旧地址：", str)
print("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
str = "this is string example....wow!!! is is"
print(str.replace("is", "was", 3))


print('rfind()'.center(100, '-'))
# rfind()：返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
# 类似于find()函数，不过是从右边开始查找
# str.rfind(str, beg=0 end=len(string))
# str -- 查找的字符串
# beg -- 开始查找的位置，默认为0
# end -- 结束查找位置，默认为字符串的长度
str1 = "this is really a string example....wow!!!"
str2 = "is"
print(str1.rfind(str2))
print(str1.rfind(str2, 0, 10))
print(str1.rfind(str2, 10, 0))
print(str1.find(str2))
print(str1.find(str2, 0, 10))
print(str1.find(str2, 10, 0))


print('rindex()'.center(100, '-'))
# rindex()：返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，可以指定可选参数[beg:end]设置查找的区间。
# 类似于index()函数，不过是从右边开始查找
# str.rindex(str, beg=0 end=len(string))
# str -- 查找的字符串
# beg -- 开始查找的位置，默认为0
# end -- 结束查找位置，默认为字符串的长度
str1 = "this is really a string example....wow!!!"
str2 = "is"
print(str1.rindex(str2))
# print(str1.rindex(str2, 10))  # 异常


print('split()'.center(100, '-'))
# split()：通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
# str.split(str="", num=string.count(str))
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。
str = "this is string example....wow!!!"
print(str.split( ))       # 以空格为分隔符
print(str.split('i', 1))   # 以 i 为分隔符
print(str.split('w'))     # 以 w 为分隔符
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)
print(x)

# URL 简单分割（获取图片名称）
url = "http://www.baidu.com/python/image/123456.jpg"
path = url.split(".")
print(path)
path = url.split("/")
print(path)
picname = path[-1]
print(picname)


print('splitlines()'.center(100, '-'))
# splitlines()：按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表
# 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
sp = 'ab c\n\nde fg\rkl\r\n'.splitlines()
print(sp)
sp = 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
print(sp)


print('startswith()'.center(100, '-'))
# startswith()：用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
# str.startswith(substr, beg=0,end=len(string))
# str -- 检测的字符串。
# substr -- 指定的子字符串。
# strbeg -- 可选参数用于设置字符串检测的起始位置。
# strend -- 可选参数用于设置字符串检测的结束位置。
str = "this is string example....wow!!!"
print(str.startswith('this'))   # 字符串是否以 this 开头
print(str.startswith('string', 8))  # 从第八个字符开始的字符串是否以 string 开头
print(str.startswith('this', 2, 4)) # 从第2个字符开始到第四个字符结束的字符串是否以 this 开头


print('strip()'.center(100, '-'))
# strip()：用于移除字符串头尾指定的字符（默认为空格）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# 如果不带参数，默认是清除两边的空白符，例如：/n, /r, /t, ' ')
# 带有参数的时候，这个参数可以理解一个要删除的字符的列表
# 字符串最开头和最结尾是不是包含要删除的字符，如果有就会继续处理，没有的话是不会删除中间的字符的。
# str.strip([chars]);
# chars -- 移除字符串头尾指定的字符序列。
str = "*****this is **string** example....wow!!!*****"
print(str.strip('*'))
str = "123abcrunoob321"
print(str.strip('12'))
addr = '123@163.com'
print(addr.strip('12'))
print(addr.strip('23m'))
str = '123132231213321312==321312213231123132'
print(str.strip('123'))


print('swapcase()'.center(100, '-'))
# swapcase()：用于对字符串的大小写字母进行转换。
# str.swapcase()
str = "this is string example....wow!!!"
print(str.swapcase())
str = "This Is String Example....WOW!!!"
print(str.swapcase())


print('title()'.center(100, '-'))
# title()：返回"标题化"的字符串, 就是说所有单词的首个字母转化为大写，其余字母均为小写(见istitle())
# 非字母后的第一个字母将转换为大写字母
# str.title();
str = "this is string example from runoob....wow!!!"
print(str.title())
txt = "hello b2b2bb2 and 3g3g3gg"
print(txt.title())


print('translate()'.center(100, '-'))
# translate()：根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
# str.translate(table)
# bytes.translate(table[, delete])
# bytearray.translate(table[, delete])
# table -- 翻译表，翻译表是通过 maketrans() 方法转换而来。
# deletechars -- 字符串中要过滤的字符列表。
# 根据 python3.7.3 文档，str 类型的 translate() 函数只接受一个参数
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表
str = "this is string example....wow!!!"
print(str.translate(trantab))
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))


print('upper()'.center(100, '-'))
# upper()：将字符串中的小写字母转为大写字母。
# str.upper()
str = "this is string example from runoob....wow!!!";
print(str.upper())


print('zfill()'.center(100, '-'))
# zfill()：返回指定长度的字符串，原字符串右对齐，前面填充0。
# str.zfill(width)
# width -- 指定字符串的长度。原字符串右对齐，前面填充0
# zfill(width) 作用同 rjust(width, '0')
str = "this is string example from runoob....wow!!!"
print(str.zfill(40))
print(str.zfill(50))
print(str.rjust(50, '0'))



