#include <stdio.h>
// #include <curses.h>
#include "conio.h"

int main()
{
    while(!kbhit())
    {
        printf("Press a key\n");
    }
    return 0;
}
