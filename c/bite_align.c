#include<stdio.h>
 
typedef struct {
 
    int i;  //4
    char a; //1
    char b; //1
    char c; //1
            //1
 
}Test1;
 
typedef struct {
 
    int i;  //4
    char a; //1
    char b; //1
    char c; //1
 
}__attribute__((packed))Test2;
 
typedef struct {
 
    int i;  //4
    char a; //1
    char b; //1
    char c; //1
 
}__attribute__((__packed__))Test3;
 
int main(int argc, char *argv[])
{
 
    printf("Test1 = %d \r\n",sizeof(Test1));
    printf("Test2 = %d \r\n",sizeof(Test2));
    printf("Test3 = %d \r\n",sizeof(Test3));
 
    return 0;
}

