# -*- coding:utf-8 -*-

#从一组数据中去除掉重复的元素，并将其排序输出

a = [4, 7, 3, 4, 1, 9, 8, 3, 7]
# print(type(a))
b = set()
for x in a:
    b.add(x)
print(sorted(b))

#***可以直接将list变成set***
print(sorted(set(a)))