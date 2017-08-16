# -*- coding:utf-8 -*-
# list 常用操作


# list定义
li = ["a", "mpilgrim", "z", "example"]

#------------索引
print(li[1],li[-1])
#注意此时没有显示最后一个元素
print(li[1:-1])

#------------增加元素
li.append("new")
li.insert(2,"insert")
#增加多个元素
li.extend(["one","new"])
print(li)


#-------------搜索
print(li.index("example" ))
#返回FALSE
print("c" in li)


#-------------删除元素
print('--------删除元素--------')
li.remove('z')
#删除首次出现的一个值
li.remove('new')

print(li)
del li[1:3]
print("del",li)
#pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
li.pop()

#-------------运算符
print(li+ ['exam', '+'])
print([1, 2] * 3)
#-------------使用join链接list成为字符串
print(";".join(li))
#-------------split分割字符串,将字符串变成数组
s = 'server=mpilgrim;uid=sa;database=master;pwd=secret'
print("split:",s.split(";"))
#-------------list的映射解析
print('--------映射解析--------')
li2 = [1, 9, 8, 4]
print([x*2 for x in li2])

#-------------dictionary中的解析
print('--------dictionary中的解析--------')
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k,v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])
#-------------list过滤
print('--------list过滤--------')
li3 = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li3 if len(elem) > 1])
print([elem for elem in li3 if elem != "b"])