#include <stdio.h>

int main()
{
    int max(int x, int y);
    int a, b, c;
    printf("Enter two number:\n");
    scanf("%d%d", &a, &b);
    c = max(a, b);
    printf("Max is %d\n", c);
    
    return 0;
}

int max(int x, int y)
{
    int z;
    z = x > y ? x : y;
    return z;
}
