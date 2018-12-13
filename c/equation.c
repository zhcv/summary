#include <stdio.h>
#include <math.h>

/* Program to solve the quadratic equation
 * a*x*x + b*x + c = 0 */

int main(void) {
    float a,b,c;
    float Delta;
    float root1, root2;
    float root_real;
    float root_imag;

    printf("a, b, c ? ");
    scanf("%f %f %f", &a, &b, &c);


    Delta = b * b - 4.0 * a * c;

    if (Delta > 0)
    {
	root1 = 0.5 * (-b + sqrt(Delta))/a;
	root2 = 0.5 * (-b - sqrt(Delta))/a;
	printf("The quadratic has two real roots: \n");
	printf("%f and %f\n", root1, root2);
    }
    else // Two complex roots
    {
	root_real = -0.5 * b / a;
	root_imag = 0.5 * sqrt(-Delta) / a;
	printf("The quadratic has two complex roots: \n");
	printf("%f + i%f\n", root_real, root_imag);
	printf("%f - i%f\n", root_real, root_imag);
    }
    return 0;
}
