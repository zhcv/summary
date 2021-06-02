#include <iostream>
#include <stdio.h>

using namespace std;

class Parent
{
public:
    Parent(int i, int j)
    {
        m_i = i;
        m_j = j;
        cout << "Parent(int i, int j): " << this << endl;
    }
    virtual void print()
    {
        cout << "Parent::" << __func__<< endl;
        cout << "m_i = "<< m_i << endl;
        cout << "m_j = "<< m_j << endl;
    }
    virtual void sayHello()
    {
        cout << "Parent::sayHello()" << endl;
    }
    virtual void func()
    {
        cout << "Parent::func()" << endl;
    }
    virtual ~Parent()
    {
        cout << "~Parent(): " << this << endl;
    }
    static void display()
    {
        cout << "Parent::display()" << endl;
    }
    int add(int v)
    {
        return m_i + m_j + v;
    }
protected:
    int m_i;
    int m_j;
};

int main(int argc, char *argv[])
{
    cout <<&Parent::display<<endl;
    cout <<&Parent::print<<endl;
    cout <<&Parent::sayHello<<endl;
    cout <<&Parent::func<<endl;

    return 0;
}
