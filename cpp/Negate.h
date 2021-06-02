#ifndef NEGATE_H
#define NEGATE_H 

#include <iostream>

using namespace std;


class Negate
{
    public:
        int operator()(int) { return -n;}
}


void Callback(int n, Negate & neg)
{
    int val = neg(n); // call overload func
    cout << val << endl;
}


#endif // NEGATE_H
