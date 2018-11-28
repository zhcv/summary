#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main()
{
    int c;
    c = add(20, 30);
    printf("c = %d\n", c);
    return 0;
}
