#include <ctype.h>
#include <stdio.h>

int main()
{
    char ch = 'A';
    if(isupper(ch))
        printf("\nEntered character is uppercase character\n");
    else
        printf("\nEnterd character is not uppercase character\n");
    return 0;
}
