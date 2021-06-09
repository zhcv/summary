#include <stdio.h>


int main(int argc, char *argv[])
{
    FILE *fp;
    char buf[1024];
    char* TagName=(char*)malloc(sizeof(char)*60);
    

    fp = fopen(argv[1], "r");
    while(fgets(buf, sizeof(buf), fp))
    {
        memcpy(TagName, buf, 28);
        memset(TagName[29], '1', sizeof(char)*1);
        //TagName[28] = 28 + '\0';
        // TagName[29] = 29 + '1';
        printf("%s\n", TagName);
    }
    fclose(fp);

    return 0;
}
