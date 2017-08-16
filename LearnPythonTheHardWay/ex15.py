# -*- coding: utf-8 -*-
#打开文件、读取文件
from sys import argv

script, filename = argv
#编译时获取文件名
txt = open(filename)
#读取文件并打印
print "Here's your file %r:" % filename
print txt.read()
#咋程序运行过程中获取文件名
print "Type the filename again:"
file_again = raw_input(">")
#打开文件
txt_again = open(file_again)
#读取文件并打印
print txt_again.read()
