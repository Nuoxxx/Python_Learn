# coding:utf8
'''
Created on 2017��4��26��

@author: kaiyue
'''
import urllib.request




class HtmlDownloader(object):
    
    
    def download(self,url):
        print("download")
        if url is None:
            print("None")
            return None
        
        respon = urllib.request.urlopen(url)
        print("None 0")
        if respon.getcode() != 200:
            print("None 200")
            return None
        print(respon.read())
        return respon.read()
        
    
    



