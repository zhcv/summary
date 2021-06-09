#include <stdio.h>


typedef union{

    char c;
    int a;
    int b;
} Demo;


int main(int argc, char *argv[])
{
    Demo d;
    d.c = 'H';
    d.a = 10;
    // d.b = 12;

    printf("size: %d\n", sizeof(d));
    printf("\n");
    printf("%c\%d\t\n", d.c, d.a);

    return 0;
}
