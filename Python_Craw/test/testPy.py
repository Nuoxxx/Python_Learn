# coding:utf-8


import urllib.request


url = "http://www.baidu.com"

print("第一种方法")
response = urllib.request.urlopen(url)
print(response.getcode())
print(response.read())
