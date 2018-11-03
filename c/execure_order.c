#include <stdio.h>

int main()
{
    /* below two func declaration methods are both ok.
     * int f(int a, int b);
     */
    int f(int, int);
    int i = 2, p;
    p = f(i, ++i);
    printf("%d\n", p);

    return 0;
}

int f(int a, int b)
{
    int c;
    if(a>b) c = 1;
    else if(a == b) c = 0;
    else c = -1;
    
    return c;
}
