#include <stdio.h>

void main()
{
    int max(float x, float y);
    float a, b;
    int c;
    printf("Enter two numbers:\n");
    scanf("%f%f", &a, &b);
    printf("a = %.2f, b = %.3f\n", a, b);
    c = max(a, b);
    printf("Max number is %d\n", c);
}

int max(float x, float y)
{
    float z;
    z = x > y ? x : y;
    return z;
}
