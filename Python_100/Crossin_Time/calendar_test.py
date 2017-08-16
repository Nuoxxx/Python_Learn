# -*- coding:utf-8 -*-
# calendar日期使用
import calendar

monthRange = calendar.month(2016, 9)
print(monthRange)

# 获取某个月的日历，返回字符串类型
calendar.setfirstweekday(calendar.SUNDAY) # 设置日历的第一天
cal = calendar.month(2015, 12)
print(cal)
 
# 获取一年的日历
cal = calendar.calendar(2015)
print(cal)
cal = calendar.HTMLCalendar(calendar.MONDAY)
print(cal.formatmonth(2015, 12))

# 判断是否闰年、两个年份之间闰年的个数
print(calendar.isleap(2017))
print(calendar.leapdays(2010, 2019))

