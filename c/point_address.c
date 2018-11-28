/*
 * =====================================================================================
 *
 *       Filename:  point_address.c
 *
 *    Description:  Variable store address
 *
 *        Version:  1.0
 *        Created:  11/22/2018 12:45:34 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include <stdio.h>

int main()
{
    int i = 39;
    printf("i = %d\n", i);
    printf("dizhi =  %04x\n", &i);
    char a, *pa;
    a = 10;
    printf("a = %d\n", a);
    pa = &a;
    *pa = 20;
    printf("a = %d\n", a);



    return 0;
}
