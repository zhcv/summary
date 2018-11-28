#include <stdio.h>

int main()
{
    char buf[15];
    printf("Enter a string: \n");
    gets(buf);
    printf("string is: %s\n", buf);
    return 0;
}
