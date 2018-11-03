#include <stdio.h>

void main()
{
    void print_star(); //declararion function
    void print_message();

    print_star(); // call function
    print_message();
    print_star();
}

void print_star(){
    printf("******************************\n");
}

void print_message(){
    printf("      how do you do!\n");
}
