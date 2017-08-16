# -*- coding: utf-8 -*-
#格式字符串
name = 'Zed A. Shaw'
age = 27
# 1 inch = 2.54cm
height = 160 #inches
# 1 pound = 0.4536KG
weight = 56 #lbs
eyes = 'Black'
teeth = 'White'
hair = 'Brown'
# %s String  %d 有符号的十进制数  %c 字符
print "Let's talk about %s." % name
print "His age is %c." % age
print "He's %f inches tall." % (height*2.54)
print "He's %d pounds heavy." % weight
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d,%d, and %d I get %d." %(age, height, weight, age + height + weight)
