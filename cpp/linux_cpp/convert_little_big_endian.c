#include <stdio.h>
 
unsigned int reverse_byte(char *c, char num)
{
    unsigned int r = 0;
    int i;
    for (i=0; i<num; i++)
    {
        r |= (*(c+i)<<(((num-1)*8)-8*i));
    }
    return r;
 
}
 
int main()
{
    int data = 0x12345678;
    int i = 0;
    char s;
    unsigned int out;
    while(1)
    {
    scanf("%d", &i);
    out = reverse_byte((char*)(&data), (char)i);
    printf("%x\n", out);
    }
}
