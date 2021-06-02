
union little_big_endian
{
    int b;
    struct
    {
        bool is_lttle;
        bool other[3];
    }u;
};


bool is_little_endian()
{
    little_big_endian lbe;
    lbe.b = 1;
    if( lbe.u.is_lttle )
    {
        return true;
    }
    else
    {
        return false;
    }
 
}



void convert_endian_32(void *data)
{
    //交换第0个字节和第3个字节
    data[0]=data[0]^data[3]
    data[3]=data[0]^data[3]
    data[0]=data[0]^data[3]
    
    //交换第1个字节和第2个字节
    data[1]=data[1]^data[2]
    data[2]=data[1]^data[2]
    data[1]=data[1]^data[2]
}

/*
简单来说：大端——高尾端，小端——低尾端

举个例子，比如数字 0x12 34 56 78在内存中的表示形式为：

1)大端模式：

低地址 -----------------> 高地址

0x12  |  0x34  |  0x56  |  0x78

2)小端模式：

低地址 ------------------> 高地址

0x78  |  0x56  |  0x34  |  0x12

可见，大端模式和字符串的存储模式类似。
*/


