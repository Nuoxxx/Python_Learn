# Override Explicitly 重写父类方法
class Parent(object):
    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self):
        print "ChILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
