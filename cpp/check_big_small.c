#include <stdio.h>

void out()
{
    short i = 0x1122;
    char *a = (char*)(&i);
    printf ("0x%x\n", *(a + 0)); //大端为 0x11 小端为 0x22
    printf ("0x%x\n", *(a + 1));
}


int main (void)
{
    union
    {
        short i;
        char a[2];
    }u;
    u.a[0] = 0x11;
    u.a[1] = 0x22;
    printf ("0x%x\n", u.i);  //0x2211 为小端  0x1122 为大端
    
    out();
    return 0;
}
