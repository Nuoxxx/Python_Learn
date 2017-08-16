# -*- coding:utf-8 -*-
import time
import datetime
# 获取当前时间，返回的是struct_time元组
print(time.localtime())
# 暂停1S
#time.sleep(1)
#获取格式化的时间   Mon May 15 11:55:46 2017
print(time.asctime())
print("-------------------")
#strptime---把字符串转换为时间
print(datetime.datetime.strptime("2014-3-1","%Y-%m-%d"))
print(datetime.datetime.strptime("2005-2-16","%Y-%m-%d")-datetime.datetime.strptime("2004-12-31","%Y-%m-%d"))
print("-------------------")
#格式化成2017-05-15 14:06:45形式    strftime---把时间转化为字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#格式化成Mon May 15 14:11:15 2017 形式
print(time.strftime("%a %b %d %H:%M:%S %Y",time.localtime()))
#格式化成05/15/17 14:23:56
print(time.strftime("%D %H:%M:%S",time.localtime()))
print("-------------------")
#将格式字符串转换为时间戳
a = "Mon May 15 14:09:48 2017"
print("从时间获取时间戳：",time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
print("从时间戳获取日期:",datetime.date.fromtimestamp(1494852797.0))
print("从时间戳获取时间（日期和时间）:",datetime.datetime.fromtimestamp(1494852797.0))


