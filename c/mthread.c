#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
 
void *new_thread (void *arg)
{
    printf("A new Thread Created!\n");
    return arg;
}
 
int main ()
{
    pthread_t tid;
    int checking;
    checking = pthread_create(&tid, NULL, new_thread, NULL);
    if (checking !=0)
    perror("create Thread");
    pthread_exit(NULL);
}
