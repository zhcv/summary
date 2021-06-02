#include <stdio.h>

int main(int args, char *argv[])
{
    union {
        short i;
        char a[2];
    }u;
    u.a[0] = 0x11;
    u.a[1] = 0x22;
    
    printf("0x%x\n", u.i);  //0x2211 wei little endian, 0x1122 big endian
    
    return 0;
}
