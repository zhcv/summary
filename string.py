# coding:utf-8
'''''
Created on 2017年3月5日

@author: zxt
'''
#from io import StringIO
from io import BytesIO as StringIO

# StringIO还有一个对应的c语言版的实现，它有更好的性能，但是稍有一点点的区别:
# cStringIO没有len和pos属性。（还有，cStringIO不支持Unicode编码）
# 如果实例化一个带有默认数据的cStringIO.StringIO类。那么该实例是read-only的;
# 无默认参数的是cStringIO.StringO，它是可读写的。cs = cStringIO.StringO()

# StringIO模块主要用于在内存缓冲区中读写数据。模块是用类编写的，只有一个StringIO类，
# 所以它的可用方法都在类中。此类中的大部分函数都与对文件的操作方法类似。
# s = StringIO()
# s.write('www.baidu.com\n')
# s.write("news.realsil.com.cn")
# # getvalue() 方法用于获取写入后的str
# print(s.getvalue())
#
# # 也可以像读取文件一样读取StringIO中的数据
# s.seek(0)
# while True:
#     strBuf = s.readline()
#     if strBuf == "":
#         break
#
#     print strBuf.strip()
#
# s.close()

# 可以用一个str初始化StringIO
ss = StringIO("Hello!\nGoodBay!".encode('utf-8'))
ss.seek(0)
print ss.read().split('\n')
ss.close()

# StringIO 模块中的函数：
# s.read([n])
# 参数n限定读取长度，int类型；缺省状态为从当前读写位置读取对象s中存储的所有数据。读取结束后，读写位置被移动。
#
# ----------------------
# s.readline([length])
# 参数length限定读取的结束位置，int类型，缺省状态为None：从当前读写位置读取至下一个以“\n”为结束符的当前行。读写位置被移动。
#
# ----------------------
#
# s.readlines([sizehint])
# 参数sizehint为int类型，缺省状态为读取所有行并作为列表返回，除此之外从当前读写位置读取至下一个以“\n”为结束符的当前行。读写位置被移动。
#
# ----------------------
# s.write(s)
# 从读写位置将参数s写入给对象s。参数s为str或unicode类型。读写位置被移动。
#
# ----------------------
# s.writelines(list)
# 从读写位置将list写入给对象s。参数list为一个列表，列表的成员为str或unicode类型。读写位置被移动。
#
# ----------------------
# s.getvalue()
# 此函数没有参数，返回对象s中的所有数据。
#
# ----------------------
# s.truncate([size])
# 从读写位置起切断数据，参数size限定裁剪长度，缺省值为None。
#
# ----------------------
# s.tell()
# 返回当前读写位置。
#
# ----------------------
# s.seek(pos[,mode])
# 移动当前读写位置至pos处，可选参数mode为0时将读写位置移动至pos处，为1时将读写位置从当前位置起向后移动pos个长度，
# 为2时将读写位置置于末尾处再向后移动pos个长度；默认为0。
#
# ----------------------
# s.close()
# 释放缓冲区，执行此函数后，数据将被释放，也不可再进行操作。
#
# ----------------------
# s.isatty()
# 此函数总是返回0。不论StringIO对象是否已被close()。
#
# ----------------------
# s.flush()
# 刷新内部缓冲区。
#
# from io import BytesIO
#
# # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# b = BytesIO()
# b.write("hello".encode("utf-8"))
# b.seek(0)
# print(b.read())
# b.close()