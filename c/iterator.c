#include <stdio.h>

int iterator(int value)
{
    if (value == 1)
	return 1;
    return iterator(value -1) + value;
}

int main(void) {
    printf("%d\n", iterator(10));
    return 0;
}
