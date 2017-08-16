# -*- coding: utf-8 -*-
from urllib.parse import urlparse,urlunparse, urlsplit, urljoin, urlunsplit,SplitResult

url = "https://www.google.com.hk:8080/home/search;12432?newwi.1.9.serpuc#1234"  

p = urlparse(url)
#ParseResult(scheme='https', netloc='www.google.com.hk:8080', path='/home/search', params='12432', query='newwi.1.9.serpuc', fragment='1234')
#ParseResult类还有几个常用方法：res.username/res.password/res.hostname/res.port/res.geturl()
print(p)
print(p.port,p.hostname)
print(p.geturl())  
#SplitResult(scheme='https', netloc='www.google.com.hk:8080', path='/home/search;12432', query='newwi.1.9.serpuc', fragment='1234')
r = urlsplit(url)  
print(r)  
#unparse
parts = ["http","www.facebook.com","/home/email","132","parts","md5=?"]  
print("unparse:****"+urlunparse(parts))
print (urlunsplit(parts[0:5])) 

base = "http://baidu.com/home"  
url = "index.html" 
#http://baidu.com/index.html 
print(urljoin(base, url))  
base = "http://baidu.com/home/action.jsp"  
url = "index.html"  
#http://baidu.com/home/index.html
print(urljoin(base, url))  
base = "http://baidu.com/home/action.jsp"  
url = "/index.html"  
#http://baidu.com/index.html
print(urljoin(base, url))  
base = "http://baidu.com/home/action.jsp"  
url = "../../../index.html" 
# http://baidu.com/index.html
print(urljoin(base, url))  
