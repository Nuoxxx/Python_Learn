# -*- coding: utf-8 -*-
import urllib.request 
import re
from bs4 import BeautifulSoup
# 获取慕课网的图片
url = "http://coding.imooc.com/"

response = urllib.request.urlopen(url)
data = response.read()
#print(data)
##这行很重要
data = data.decode('utf-8')
pic_urls=re.findall(r'http://.+\.jpg', data)


i = 0
for pic_url in pic_urls:
    print(pic_url)
#默认获取出来的url中包含http://coding.imooc.com/class/96.html?mc_marking=f1b4d61bb5a5ef25159a094a7039f112&mc_channel=codingshouyebanner" data-track="szbanner-1-1" target="_blank" style="background-image: url(http://img.mukewang.com/590bf028000172df05900120.jpg
#将不符合规范的URL剔除
    if re.match(r'http://sz.*.jpg', pic_url):        
        f = open(str(i)+'.jpg','wb')
        req = urllib.request.urlopen(pic_url)
        buf = req.read()
        f.write(buf)
        i+=1