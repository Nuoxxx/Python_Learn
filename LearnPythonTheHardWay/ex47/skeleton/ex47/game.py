# -*- coding:utf-8 -*-
class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        #paths是字典
        self.paths = {}


    def go(self, direction):
        #dict.get(key, default=None)  返回指定键的值，如果值不在字典中返回默认值None
        return self.paths.get(direction, None)

    def add_path(self, paths):
        self.paths.update(paths)
