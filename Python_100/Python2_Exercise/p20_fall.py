#-*- coding:utf-8 -*-
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height = 100.0
tim = 10

heights = []

for i in range(1,tim):
    #本次下落高度为上次高度一半   
    height/=2
    heights.append(height)
print(height/2)
print(100+sum(heights)*2)
