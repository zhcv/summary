#include <iostream>

using namespace std;


int main()
{
    int i = 9;
    int * const p = &i;
    i = 99;
    cout << "p = " << *p << endl;
    return 0;
}
