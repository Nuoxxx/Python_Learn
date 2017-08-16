# coding:utf8
'''
Created on 2017��4��26��

@author: kaiyue
'''


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        for url in self.new_urls:
            print("url:"+url)
    
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):
        a = len(self.new_urls)
        print("len:"+str(a))
        return len(self.new_urls)!=0

    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        print("返回的url:"+new_url) 
        return new_url
        
        

    
    
    
    
    
    
    
    
    
    



