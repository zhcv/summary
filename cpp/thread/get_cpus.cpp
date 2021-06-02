#include<iostream>
#include<thread>
using namespace std;

// g++ -std=c++11 get_cpus.cpp -lpthread -o cpus

int main()
{
    auto n = thread::hardware_concurrency();//获取cpu核心个数
    cout << n << endl;
    return 0;
}
