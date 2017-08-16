# -*- coding:utf-8 -*-

ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ",next_one
    stuff.append(next_one)
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."
# Oranges
print stuff[1]
# Corn
print stuff[-1]
# Corn
print stuff.pop()
# str.join(sequence)  -- sequence 表示要连接的元素序列
# Apple Oranges Crows Telephone Light Sugar Boy Girl Banana
print ' '.join(stuff)
#  打印结果  Telephone#Light
print '#'.join(stuff[3:5])
