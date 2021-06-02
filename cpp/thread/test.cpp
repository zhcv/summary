#include <thread>
#include <iostream>


// g++ -std=c++11 test.cpp -o test -lpthread

class Greet
{
    const char *owner = "Greet";
public:
    void SayHello(const char *name) {
        std::cout << "Hello " << name << " from " << this->owner << std::endl;
    }
};
int main() {
    Greet greet;

    std::thread thread(&Greet::SayHello, &greet, "C++11");
    thread.join();

    return 0;
}
//输出：Hello C++11 from Greet
