"""
class A(object):
    def __init__(self): pass
    def showw(self):
        print "A"

class B(A):
    def __init__(self):
        super(B, self).__init__()
        pass
    def show(self):
        print "B"
"""
# method_2
class A:
    def __init__(self): pass
    def showw(self):
        print "A"

class B(A):
    def __init__(self):
        A.__init__(self)
    def show(self):
        print "B"

obj = B()
print(obj.__class__)
obj.show()
obj.showw()
