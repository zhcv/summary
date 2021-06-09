#include <iostream>
#include <chrono>

/* -std=c++11 or -std=gnu++11 */

using std::chrono::nanoseconds;
using std::chrono::duration_cast;

int main(int argc, char* argv[])
{

    std::cout << "resolution (nano) = " << (double) std::chrono::high_resolution_clock::period::num
        / std::chrono::high_resolution_clock::period::den * 1000 * 1000 * 1000 << std::endl;


    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << "how much nanoseconds std::cout takes?" << std::endl;

    auto t2 = std::chrono::high_resolution_clock::now();
    auto diff = t2-t1;

    nanoseconds ns = duration_cast<nanoseconds>(diff);

    std::cout << "std::cout takes " << ns.count() << " nanoseconds" << std::endl;

    return 0;

}
