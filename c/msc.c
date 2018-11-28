#include <stdio.h>

#define INCREMENT(x) ++x
#define merge(a, b) a##b
#define get(a) #a
#define PRINT(i, limit) while(i < limit) \
    { \
        printf("GeeksQuiz "); \
        i++; \
    }


int main()
{
    char *ptr = "GeeksQuiz";
    int x = 10;
    printf("%s\n", INCREMENT(ptr));
    printf("%d\n", INCREMENT(x));
    
    int a = 12;
    int b = 34;
    int c;
    printf("merge ab is %d\n", merge(123, 456));
    printf("c = %s\n", get(helloworld));
    printf("\n");
    int i = 0;
    PRINT(i, 3);
    printf("\n");
    return 0;
}
