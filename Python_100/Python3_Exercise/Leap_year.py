# -*- coding:utf-8 -*-
#判断是否是闰年
year = int(input("请输入年份："))

if(year % 4 ==0):
    if(year% 100 == 0):
        if(year % 400 ==0):
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))

#在Calendar源码中看到的写法，更简洁
def isleap(year):
    return year % 4 ==0 and (year % 100 !=0 or year % 400 ==0)

print(isleap(year))