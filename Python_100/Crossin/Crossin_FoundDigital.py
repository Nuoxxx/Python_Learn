# -*- coding:utf-8 -*-

# 字符串  text = "aAsmr3idd4bgs7Dlsf9eAF" 
# 请将text字符串中的数字取出，并输出成一个新的字符串

import re
text = "aAsmr3idd4bgs7Dlsf9eAF" 
p = re.compile(r'\d+')
str = ''
for m in p.finditer(text):
#     print(m.group())
    str +=m.group()
print(str)


#网上解决方案
#***join的使用***
print("".join(re.findall(r'[\d]+',text)))

print("".join([i for i in text if i.isdigit()]))

print("".join(filter(lambda x: x.isdigit(),text)))
#返回所有字母
print("".join(filter(lambda x: x.isalpha(),text)))
#返回大写字母
print("".join(filter(lambda x: x.isupper(),text)))

print(list(filter(lambda x:True if x%3 ==0 else False ,range(100))))