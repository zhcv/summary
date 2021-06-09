import ctypes

def callfoo(str_in):
    #print 'input:\n%s' %str_in
    #调用库
    input = ctypes.c_char_p()  #对应c指针类型 char *p
    input.value=str_in  #字符串赋值
    ll = ctypes.cdll.LoadLibrary
    lib = ll("./libcallfoo.so")  #调用so
    p=ctypes.create_string_buffer(4*len(str_in)) #申请出参的内存大小
    lib.foo(len(str_in), input, p)
    print p.raw    #出参的访问方式
