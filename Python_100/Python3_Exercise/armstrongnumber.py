# -*- coding:utf-8 -*-
#判断阿姆斯特朗数
def Is_armstrongnumber(num):
    n = len(str(num))
    
    tmp = num
    while tmp>0:
# /   除     21/10 = 2.1
# //  取整除      9//2 = 4
# %   取模   21%10 = 1
        digit = tmp % 10
        sum += digit**n 
        tmp //=10
        
    if (sum == num):
        print("是阿姆斯特朗数")
    else:
        print("不是阿姆斯特朗数")

Is_armstrongnumber(153)
