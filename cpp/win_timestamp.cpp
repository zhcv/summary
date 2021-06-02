#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>
using namespace std::chrono;

int main()
{
    high_resolution_clock::time_point t1 = high_resolution_clock::now(); //返回时间戳

    // TODO

    high_resolution_clock::time_point t2 = high_resolution_clock::now();

    duration<double, std::milli> time_span = t2 - t1;

    std::cout << time_span.count()  << std::endl;

    return 0;
}
