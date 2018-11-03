#include <stdio.h>

int main()
{
    int i, len;
    char c[] = "I am a good boy!";
    len = sizeof(c);
    printf("c string's length %d\n", len);
    for(i=0;i<len;i++)
	printf("%c", c[i]);
    printf("\n");
    printf("%s", c);
    printf("\n");
    return 0;
}
