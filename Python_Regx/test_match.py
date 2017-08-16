# -*- coding: utf-8 -*-
# 学习match对象对应的属性和方法
import re
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#----------------------------属性--------------------------------
print("-----------属性---------------")
# 匹配时使用的文本
print ("m.string:",m.string)
# 匹配时使用的Pattern对象    re.compile('(\\w+) (\\w+)(?P<sign>.*)')
print ("m.re:",m.re)
# 文本中正则表达式开始搜索的索引
print ("m.pos:",m.pos)
# 文本中正则表达式结束搜索的索引
print ("m.endpos:",m.endpos)
# 最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
print ("m.lastindex:",m.lastindex)
# 最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None   sign
print ("m.lastgroup:",m.lastgroup)
#--------------------------方法-----------------------------------
print("-----------方法---------------")
# 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回  ('hello', 'world')
print("m.group(1,2):",m.group(1, 2)) 
# hello world!
print("m.group():", m.group()) 
# 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。default表示没有截获字符串的组以这个值替代，默认为None
# ('hello', 'world', '!')
print("m.groups():",m.groups())
# 返回以有别名的组的别名为键、以该组截获的子串为值的字典，没有别名的组不包含在内
# {'sign': '!'}
print("m.groupdict():",m.groupdict())
# 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）
print ("m.start(2):",m.start(2))
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）
print ("m.end(2):",m.end(2))
# 返回(start(group), end(group))
# (6, 11)
print ("m.span(2):",m.span(2))
# 将匹配到的分组代入template中然后返回
# world hello!
print (r"m.expand(r'\2 \1\3'):",m.expand(r'\2 \1\3'))


