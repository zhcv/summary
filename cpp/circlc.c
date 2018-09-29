// circlc.c: 计算并输出圆的面积

#include<stdio.h>

double circularArea(double r);

int main()
{
    double radius = 1.0, area = 0.0;
    
    printf(" Areas of Circlcs\n\n");
    printf(" Radius Area\n"
    	   " = = = = = = = = = \n");
    
    area = circularArea(radius);
    printf("%8.1f %8.2f\n", radius, area);

    radius = 5.0;
    area = circularArea(radius);
    printf("%8.1f %8.2f\n", radius, area);
    
    return 0;
}

double circularArea(double r)
{
    const double pi = 3.1415926536;
    return pi * r * r;
}


