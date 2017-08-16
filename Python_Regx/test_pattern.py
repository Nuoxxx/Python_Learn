# -*- coding: utf-8 -*-
# 学习Pattern对象对应的属性和方法
import re
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
#----------------------------属性-------------------------------- 
print ("p.pattern:", p.pattern)
print ("p.flags:", p.flags)
print ("p.groups:", p.groups)
print ("p.groupindex:", p.groupindex)
#--------------------------方法-----------------------------------

#-----------match()----------------
pattern = re.compile(r'hello')
match = pattern.match('hello world!')
if match:
    print("match.group():", match.group())

#-----------search()---------------
search_match = re.search(r'world','hello world!')
if search_match:
    print("search_match.group():", search_match.group())

#-----------split()---------------
p_split = re.compile(r'\d+')
print("split:",p_split.split('one1two2three3four4'))

print(re.split(r'\d+','one1twothree3four4'))

#------------findall()-----------
print (re.findall(r'\d+','one1two2three3four4'))

#------------finditer()-----------
for m in re.finditer(r'\d+','one1two2three3four4'):
    print(m.group())

#------------sub()/subn()-----------  subn()会返回替换次数
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!' 
print (p.sub(r'\2 \1', s)) 
def func(self):
    return self.group(1).title() + ' ' + self.group(2).title() 
print (p.sub(func, s))
print (p.subn(func, s))






