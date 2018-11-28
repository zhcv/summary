/*  arr[index] is same as index[arr]
 *  C program to demonstrate that arr[0] and 0[arr] */

#include <stdio.h>

int main()
<%
    int arr[10];
    arr[0] = 1;
    printf("%d\n", 0[arr]);

    return 0;
%>
