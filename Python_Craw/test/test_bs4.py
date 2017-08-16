# coding:utf-8

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse1's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# print('获取所有的链接')
# links = soup.find_all('a')
# for link in links:
#     print(link.name,link['href'],link.get_text())
# #<title>The Dormouse's story</title>
# print(soup.title)
# #title
# print(soup.title.name)
# #The Dormouse's story
# print(soup.title.string)
# #head
# print(soup.title.parent.name)
# #<p class="title"><b>The Dormouse1's story</b></p>
# print(soup.p)
# #['title']
# print(soup.p['class'])
# #<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# print(soup.a)
# #
# print(soup.find_all('a'))
# #<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# print(soup.find(id = "link3"))
# #The Dormouse1's story    
# print(soup.p.string)
# print(soup.get_text())

soup2 = BeautifulSoup('<b class="boldest">Extremely bold</b>','html.parser',from_encoding='utf-8')
tag = soup2.b
print(tag)
print(tag.name)
print(tag.attrs)

tag.name='blockquote'
#tag的属性可以被添加，删除或修改；tag的属性操作方法和字典一样
tag['class']= 'verybold'
tag['id']=1
print(tag)
del tag['id']
#print(tag['id'])会报KeyError
print(tag.get('id'))
print(tag.get_text())