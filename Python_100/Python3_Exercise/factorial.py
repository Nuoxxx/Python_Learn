# -*- coding:utf-8 -*-
#阶乘

def MyFactorial(n):
    if n<0:
        print("数字有误")
        return
    elif (n == 0):
        return(1)
    else:
        return(n*MyFactorial(n-1))
    
print(MyFactorial(5))
