#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <limits.h>

int main(int argc, char* argv[])
{
    char *p = argv[0];   /* current filename */
    char cwd[PATH_MAX];
    if (getcwd(cwd, 64) == NULL)
    {
	perror("getcwd(), error");
	return 1;
    }
    printf("Current Working File: %s\n", p);
    strcat(cwd, ++p);
    printf("Current File Fullpath: %s\n", cwd);
    printf("Parameter number: %d\n", argc);
    int i;
    for (i=1; i<argc; i++)
    {
	printf("Parameter %d is %s\n", i, argv[i]);
    }
    return 0;
}
