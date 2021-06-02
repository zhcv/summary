#include <iostream>
#include <string.h>


unsigned char a(unsigned char i, void *j) {

    if (j == (void *)0)
    {
        std::cout << "j is nullptr" << std::endl;
        return 0;
    }
    *(unsigned char*) j = 1;
    std::cout << "j is not nullptr" << std::endl;
    return 1;
}


int main()
{
    char i = 'z';
    int p = 20;
    int *j = &p;
    int jj = a(i, j);
    std::cout << "jj = " << jj << std::endl;
    return 0;
}
