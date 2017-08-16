# -*- coding:utf-8 -*-
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
#类的文档字符串
print "Song.__doc__:", Song.__doc__
#类名
print "Song.__name__:", Song.__name__
#类定义所在的模块
print "Song.__module__", Song.__module__
#类的所有父类构成元素
print "Song.__bases__", Song.__bases__
# 类的属性（包含一个字典，由类的数据属性组成）
print "Song.__dict__", Song.__dict__
