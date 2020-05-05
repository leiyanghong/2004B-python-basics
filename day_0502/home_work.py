#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh

'''
1、输入一个日期（例如：2020-05-02）判断输入的日期是当年第几天

'''
'''
隐藏需求:
公元年数可被4整除（但不可被100整除）为闰年
但是正百的年数必须是可以被400整除的才是闰年
其他都是平年。
'''
# iyear = int(input("请输入年：\n"))
# imonth = int(input("请输入月：\n"))
# iday = int(input("请输入日：\n"))
#
#
# def checkYear(iyear):
#     return ((iyear % 4 == 0 and iyear % 100 != 0) or iyear % 400 == 0)
#
#
# tol_day = 0
# lis = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # 如果是闰年的话，2月份加一天
# if checkYear(iyear):
#     lis[2] += 1
# # 遍历一次days，对应月份中的天数,把对应的天数传递给tol_day存储
# for i in range(imonth):
#     tol_day += lis[i]
#
# print("输入的日期是当年第" + str(tol_day + iday) + "天")

# 第二种方法
'''
直接获取输入的年月日 - 1月1日的时间 = 年份总天数
'''
import datetime

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入日期:"))

t1 = datetime.datetime(year, month, day)
t2 = datetime.datetime(year, 1, 1)
# 截取计算得到的天数
print("输入的日期是当年第" + str(t1 - t2)[0:3] + "天")
