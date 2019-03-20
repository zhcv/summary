from __future__ import print_function

def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print (l)
    l.clear()

f(2)
f(3, [3,2,1])
f(3)
