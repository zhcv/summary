#include <iostream>
#include <sys/time.h>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <unistd.h>

using namespace std;
time_t clocktime()
{

time_t t= time(NULL);
std::cout<<" s秒级 ----:";
std::cout<<t<<endl;

struct timeval tv;
gettimeofday(&tv,NULL);
std::cout<<"10e6 微秒级s ----:";
std::cout<<tv.tv_sec<<"s,"<<tv.tv_usec<<"微秒"<<endl;


struct timespec tn;

cout<<"----";
clock_gettime(CLOCK_REALTIME, &tn);

std::cout<<"10e9 纳秒级s ----:";
std::cout<<tn.tv_sec<<"s,"<<tn.tv_nsec<<"纳秒"<<endl;


struct timespec current_time,last_time;
double aa=1.1234567891;
printf("double %.12f\n",aa);
cout<<"----";
clock_gettime(CLOCK_REALTIME, &last_time);
sleep(1);
std::cout<<last_time.tv_sec<<","<<last_time.tv_nsec<<endl;
clock_gettime(CLOCK_REALTIME, &last_time);
std::cout<<current_time.tv_sec<<","<<current_time.tv_nsec<<","<<pow(10,-9)<<endl;
  double delta_time = (current_time.tv_sec - last_time.tv_sec)+ (current_time.tv_nsec - last_time.tv_nsec)*pow(10,-9);
printf("double %.12f\n",delta_time);

}

void tt()
{
    struct timeval t_val;
    gettimeofday(&t_val, NULL);
    printf("start, now, sec=%ld m_sec=%d \n", t_val.tv_sec, t_val.tv_usec);
    long sec = t_val.tv_sec;
    time_t t_sec = (time_t)sec;
    printf("date:%s", ctime(&t_sec));
    struct timeval t_val_end;
    gettimeofday(&t_val_end, NULL);
    struct timeval t_result;
    timersub(&t_val_end, &t_val, &t_result);
    double consume = t_result.tv_sec + (1.0 * t_result.tv_usec)/1000000;
    printf("end.elapsed time= %fs \n", consume);
}


int main( ){
	clocktime();
    tt();
	return 0;
}
