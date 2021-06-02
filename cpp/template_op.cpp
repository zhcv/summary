#include <cstddef>
#include <iostream>


// g++ -std=gnu++0x main2.cpp -o main

template<class F, class A>
void Fwd(F f, A a)
{
    f(a);
}

void g(int* i)
{
    std::cout << "Function g called\n";
}

int main()
{
    g(NULL);           // 良好
    g(0);              // 良好

    Fwd(g, nullptr);   // 良好
    //  Fwd(g, NULL);  // 错误：不存在函数 g(int)
    return 0;
}
