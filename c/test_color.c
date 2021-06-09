#include <stdio.h>


void main()
{
    printf("\033[0;31mprogram termination abnormally!\033[0;39m\n");
    printf("\033[0;32mprogram termination abnormally!\033[0;39m\n");
    int a = 57;
    int b = 38;
    int aa, bb;
    aa = a >> 1;
    bb = b >> 1;
    printf("a = %d, b = %d\n", aa, bb);
}
