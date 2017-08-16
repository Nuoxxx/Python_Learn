# -*- coding:utf-8 -*-
import datetime

# 获取当天的日期
print(datetime.datetime.now())
print(datetime.date.today())

# 获取昨天的日期
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    print(type(today))
    return yesterday
print("昨天的日期：",getYesterday())


