#include <stdio.h>

inline int square(int x) { return x * x;}

extern inline int square(int);

int main()
{
    int x = 36 / square(6);
    printf("x = %d\n", x);
    return 0;
}
