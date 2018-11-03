#include <stdio.h>

void main()
{
    float fac(int n);
    int n;
    float y;
    printf("input an integer number:\n");
    scanf("%d", &n);
    y = fac(n);
    printf("%d! = %f\n", n, y);
}

float fac(int n)
{
    /*
     * float y=1;
     * while (n>1)
     * {
     *   y *= n;
     *	 --n;
     * }
     * return y;
     */
    float f;
    if (n < 0)
    {
	printf("n < 0, dataerror!\n");
	return 0;
    }
    else if (n == 0 || n == 1)
	f = 1;
    else
	f = fac(n-1) * n;
	
    return f;
}
