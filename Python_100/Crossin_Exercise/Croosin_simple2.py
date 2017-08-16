# -*- coding:utf-8 -*-
import re
#输入一个大于等于1的值n，输出星号（*）组成的等腰三角形，底边长为n
def triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)
triangle(5)

#乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j, "=" , i * j,end=' ')
    print()

#输入三个数，输出这三个数的最大值
# def three_Max(a,b,c):
#     tmp = a
#     if a < b:
#         tmp = b
#     if b < c:
#         tmp = c
#     print(tmp)
# 
# three_Max(53,15,8)
    

#输出从1000以内，用3、5、7去除，余数均为2的正整数
# for x in range(1,1000):
#     if(x%3 ==2 and x %5 ==2 and x %7 ==2):
#         print(x)

#***回文数***
#求所有不超过200的N值，N的平方是具有对称性质的回文数
for x in range(1,200):
    num = x * x
    re_num = int(str(num)[::-1])
    if num ==re_num:
        print("回数：",num,"N值：",x)


#提取英文单词
f = open("from.txt",'r')
t = open("to.txt",'w')

content = f.read()
f.close()

li = re.findall("[a-zA-Z]+", content)
# print("li:",li)
li.sort()
# print("sort之后：",li)
data = '\n'.join(li)
t.write(data)
t.close()