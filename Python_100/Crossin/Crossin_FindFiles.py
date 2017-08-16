# -*- coding:utf-8 -*-

# 找出指定文件夹中的所有以txt结尾的文件，包括所有嵌套的子文件夹。
import os
import re
import fnmatch
destFile = "E:\Test\中诚视通"

def findFiles(file):
#     if file.isdir():
    for filename in os.listdir(file):
#         print(filename)
        full_filename = os.path.join(file,filename)
        if os.path.isfile(full_filename):
            if re.match(r'.+\.txt\Z',full_filename):
                print("txt文档："+full_filename)
        else:
            findFiles(full_filename)           
findFiles(destFile)


#网上方法
def findfile(inputdir):
    txtlist = []
    for dirpath,dirnames,filenames in os.walk(inputdir):        
        #当前文件夹路径
        print("dirpath:",dirpath)        
        #当前文件夹中的目录
        print("dirnames:",dirnames)
        #当前文件夹中的文件
        print("filename:",filenames)
        
        for filename in filenames:            
            txtlist.append(filename)
#              txtlist.append(os.path.join(dirpath,filename))
    return fnmatch.filter(txtlist, '*.txt')
print(findfile(destFile))