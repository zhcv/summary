# -*- coding: utf-8 -*-

class A(object):
    def go(self):
        print "go A go!"
    def stop(self):
        print "stop A stop!"
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print "go B go!"

class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"
    def stop(self):
        super(C, self).stop()
        print "stop C stop!"

class D(B,C):
    def go(self):
        super(D, self).go()
        print "go D go!"
    def stop(self):
        super(D, self).stop()
        print "stop D stop!"
    def pause(self):
        print "wait D wait!"

class E(B,C): pass

print "a"
a = A()
print "b"
b = B()
print "c"
c = C()
print "d"
d = D()
print "e"
e = E()

# 说明下列代码的输出结果
print "ago"
a.go()
print "bgo"
b.go()
print "cgo"
c.go()
print "dgo"
d.go()
print "ego"
e.go()

print "astop"
a.stop()
print "bstop"
b.stop()
print "cstop"
c.stop()
print "dstop"
d.stop()
print "estop"
e.stop()

print "ap"
a.pause()
print "bp"
b.pause()
print "cp"
c.pause()
print "dp"
d.pause()
print "ep"
e.pause()
