# -*- coding:utf-8 -*-


print("Hello World")

# a = int(input("第一个数据："))
# print(type(a))
# b = int(input("第二个数据："))
# print("结果是：",(a+b))

#求和
# sum = 0
# for i in range(1,101):
#     print(i)
#     sum +=i
# print("总和："+str(sum))    

#等比数列
# def geo(q,n):
#     a = 1
#     for i in range(1,n):
#         if i == 1 :
#             print(a)
#         print(a*q)
#         a = a*q
#         
# geo(2,10)


#斐波那契数列
# def Febo(n):
#     a , b = 1 ,1
#     if (n == 2 or n ==1):
# #         print("n:",n)
#         return(1)
#     else:
#         return Febo(n-1) + Febo(n-2)
# 
# for i in range(1,10):
#     print(Febo(i))
    
#
# ***网上方法***斐波那契数列
def fibs(num):
    result = [1,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    print(result)
fibs(10)