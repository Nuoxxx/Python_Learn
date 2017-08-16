# -*- coding:utf-8 -*-
#获取101~200之间的素数
# from math import sqrt
# k = 0
# for i in range(101,201):
#     m = int(sqrt(i))
#     for j in range(2,m+1):
#         if i%j ==0:
#             break
#     else:
#         print(i)
#         k+=1
# print(k,"个素数")

#水仙花数
# for i in range(1,20000):
#     sum = 0
#     tmp = i
#     while tmp>0:
#         digit = tmp % 10
#         sum+= digit**3
#         tmp = tmp //10
# #         print("tmp:",tmp)
#     if(i ==sum):
#         print(i)
import os   
#正整数分解质因数--自己写的
# def reduceNum(num):
#     tmp = num
#     for i in range(2,tmp+1):
#         if (tmp%i==0):
#             print(i)
#             tmp = int(num/i)
#             if tmp ==1:
#                 os._exit(0)
# #             print("tmp:",tmp)
#             reduceNum(tmp)     
#          
# reduceNum(100)

#正整数分解质因数---更好的效果

num = int(input("数值："))
temp = []
while num>1:
    for i in range(2,num):
        if num%i ==0:
            temp.append(i)
            num = int(num/i)
            break
print(temp)

# #对应值
# a = int(input("输入数字:"))
# n = int(input("输入循环次数:"))
# An = []
# temp = a
# for i in range(1,n+1):
#     print(temp)
#     An.append(temp)
#     temp = int(str(a)*(i+1))
# print(sum(An))