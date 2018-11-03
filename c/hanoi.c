#include <stdio.h>

int main()
{
    void hanio(int n, char one, char two, char three);
    int m;
    printf("input the number of diskes:\n");
    scanf("%d", &m);
    printf("The step to moving %d diskes:\n", m);
    hanio(m, 'A', 'B', 'C');
    
    return 0;
}

void hanio(int n, char one, char two, char three)
{
    void move(char x, char y);
    if (n == 1)
	move(one, three);
    else
    {
	hanio(n-1, one, three, two);
	move(one, three);
	hanio(n-1, two, one, three);
    }
}

void move(char x, char y)
{
    printf("%c ----> %c\n", x, y);
}
