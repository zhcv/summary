#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// gcc -g -o segfault3 segfault3.c

void main()
{
        char *ptr = "test";
        strcpy(ptr, "TEST");
}

