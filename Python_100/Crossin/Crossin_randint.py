# -*- coding:utf-8 -*-

#随机取数:从1~n中，随机取m个数。1<=m<=n 

from random import randint
import random

def produceNum(n,m):
    for x in range(0,m):
        print(randint(1,n))
                
produceNum(10, 3)

# random.sample(range(1, n), m) 
print(random.sample(range(1,10),3))