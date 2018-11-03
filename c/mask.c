#include <stdio.h>

int main()
{
    unsigned char a, b;
    unsigned char mask = 0x38;
    a = 0xff;
    b = a & mask;
    printf("The flag is : 0x%x\n", b);
    
    return 0;
}
