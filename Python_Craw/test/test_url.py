# coding:utf-8


import urllib.request
import http.cookiejar
from setuptools.sandbox import save_path


url = "http://www.baidu.com"

print("第一种方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(response1.read())

#比较直接，但不好扩展功能
print("第二种方法")
response2 = urllib.request.Request(url,headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
    })
open_url2 = urllib.request.urlopen(response2)
data = open_url2.read()
print(data.decode())

#
print("第三种方法")
def makeMyOpenner(head={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key,value in head.items():
        elem = (key ,value)
        header.append(elem)
    opener.addheaders = header
    return opener

def saveFile(data):
    save_path = 'temp.out'
    f_obj = open(save_path,'wb')
    f_obj.write(data)
    f_obj.close()

oper = makeMyOpenner()
uop = oper.open('http://www.baidu.com', timeout= 1000)
data = uop.read()
saveFile(data)
