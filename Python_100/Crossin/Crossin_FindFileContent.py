# -*- coding:utf-8 -*-

#增加对文件内容的检索
import os
import fnmatch
def findContent(dest_dir,con):
    txtlist = []
    for root,dir,filenames in os.walk(dest_dir):
#         print(filenames)       
        for filename in filenames:
            full_name = os.path.join(root,filename)
            txtlist.append(full_name)
    txtLists = fnmatch.filter(txtlist, '*.txt')
    for txt in txtLists:               
            f = open(txt,'r')
            print("文件开始")
            while(f.readline()):
                print(f.readline())
                
findContent("E:\Test", "doc")