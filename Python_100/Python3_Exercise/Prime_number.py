# -*- coding:utf-8 -*-

#判断是否是质数

num = int(input("please input a number:"))
flag = 1
for i in range(2,num):
    if(num%i ==0):
        flag = 0
        break

if(flag):
    print(num,"是质数")
else:
    print(num,"不是质数")