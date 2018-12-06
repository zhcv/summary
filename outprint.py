# -*- coding: utf-8 -*-
r"""sys.stdout 与 print
当我们在 Python 中打印对象调用 print obj 时候，事实上是调用了 
sys.stdout.write(obj+'\n')
"""


import sys

__console__ = sys.stdout

# redirection start
# ...
# redirection end



print "hello?"
# hi = sys.stdin.readline()[:-1]

f_handle = open('out.log', 'w')

sys.stdout = f_handle

print "Hello, I am coming"

# this hello can't be viewed in concole
# this hello is in file out.log

sys.stdout = __console__

print "Redirection end"

"""
a = ''
sys.stdout = a
print "hello"
Traceback (most recent call last):
  File "outprint.py", line 29, in <module>
      print "hello"
      AttributeError: 'str' object has no attribute 'write'
# 错误很明显，就是上面强调过的，在尝试调用 sys.stdout.write() 的时候，
# 发现没有 write 方法)
"""
import sys

class __redirection__:

    def __init__(self):
        self.buff = ''
        self.__console__ = sys.stdout

    def write(self, output_stream):
        self.buff += output_stream

    def to_console(self):
        sys.stdout = __console__
        print self.buffer

    def to_file(self, file_path):
        f = open(file_path, 'w')
        sys.stdout = f
        print self.buff
        f.close()

    def flush(self):
        self.flush = ''

    def reset(self):
        sys.stdout = self.__console__

if __name__ == '__main__':
    # redirection
    r_obj = __redirection__()
    sys.stdout = r_obj

    # get output stream
    print "hello"
    print "there"

    # redirection to file
    r_obj.to_file('out.log')

    # flush buffer
    r_obj.flush()

    # reset
    r_obj.reset()
"""
测试了一下redirection类, 发现不行.
不知道为何: redir.buff 始终是空的.
修改方法:
添加属性:
self.buflist =[]

在self.write()里面添加:
self.buflist.append(out_stream)

这样就可以把打印的输出保留在了重定向的buflist属性里了.

但是还是没有搞懂: 为何级联字符串不行, 追加列表就可以.
## Answer:  字符串不可改变、而列表可动态增删改。
"""
