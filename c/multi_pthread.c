#include <unistd.h>  
#include <pthread.h>  

#define NUM 10
int count;

void* thread_func(void *arg) 
{
    count++;
    printf("count %d\n", count);
    return;
}

int main()
{
    pthread_t tid[NUM];
    int i = 0;
    
    for (i = 0; i < NUM; i++)
    {
        pthread_create(&tid[i], NULL, thread_func, NULL);   
    }

    sleep(1);
    
    return 0;
}
