#!/usr/bin/env python
# -*- coding: utf-8 -*-
# blog.ithomer.net
 
class Cls(object):
    def __init__(self):
        self.__x = None
    
    def getx(self):
        return self.__x
    
    def setx(self, value):
        self.__x = value
        
    def delx(self):
        del self.__x
        
    x = property(getx, setx, delx, 'set x property')
 
if __name__ == '__main__':
    c = Cls()
    c.x = 100
    y = c.x
    print("set & get y: %d" % y)
    
    del c.x
    # del y
    vy = 'y' in locals() or 'y' in globals()
    print vy
    print vars()
    print("del c.x & y: %d" % y)   


