#include <stdio.h>    
#include <iostream>
#include <sys/time.h>      

using namespace std;


int64_t getCurrentTime()      //直接调用这个函数就行了，返回值最好是int64_t，long long应该也可以
{    
   struct timeval tv;    
   gettimeofday(&tv, NULL);    //该函数在sys/time.h头文件中
   return tv.tv_sec * 1000 + tv.tv_usec / 1000;    
}    
    

int main()    
{    
    cout << "nowTime: " << getCurrentTime() << endl;    //如果想要到秒级别的，只要除以1000就行了
    return 0;    
}
