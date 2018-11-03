#include <stdio.h>
#include <string.h>


int main(){
    char string[20];
    char str[3][20];

    int i;
    for(i=0;i<=2;i++)
	gets(str[i]);

    if(strcmp(str[0], str[1]) > 0)

