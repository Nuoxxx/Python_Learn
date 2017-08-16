# -*- coding:utf-8 -*-


# Implicit Inheritance 隐式继承
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    # tell python that you want an empty block，如果没有这行，编译的时候会报错
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
