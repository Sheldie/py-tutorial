# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'

# 输出日历
# 引入日历模块
import calendar
import datetime

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
calendar.setfirstweekday(firstweekday=6)  # 设置第一天是星期天

# 显示日历
print(calendar.month(yy, mm))

# 计算每个月天数
monthRange = calendar.monthrange(2016, 9)
print(monthRange)
# 输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），第二个元素是这个月的天数。
# 以上实例输出的意思为 2016 年 9 月份的第一天是星期四，该月总共有 30 天。
print(calendar.mdays)


# 获取昨天日期
def getYesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    # today = datetime.date.today()
    # oneday = datetime.timedelta(days=1)
    # yesterday = today - oneday
    return yesterday


# 输出
print(getYesterday())
