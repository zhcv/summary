#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* strlwr(char* s)
{
    char* tmp = s;

    for (;*tmp;++tmp) {
        *tmp = tolower((unsigned char) *tmp);
    }
    return s;
}

char* strupr(char* s)
{
    char* tmp = s;

    for (;*tmp;++tmp) {
        *tmp = toupper((unsigned char) *tmp);
    }
    return s;
}

int main()
{
    char ss[30] = "People's Republic of";
    char sr[] = " China";
    printf("ss length %zu\n", sizeof(ss));
    printf("ss length %zu\n", strlen(ss));
    printf("sr length %zu\n", sizeof(sr));
    printf("%s\n", strcat(ss, sr));

    printf("China length %ld\n", strlen("China"));

    strupr(sr);
    printf("%s\n", sr);

    return 0;
}
