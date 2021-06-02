#include <iostream>

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
    //静态成员函数
    cout << "static member function addree:" << endl;
    printf("0x%p\n", &Parent::display);
    printf("0x%p\n", Parent::display);
    //普通成员函数
    cout << "normal member function addree:" << endl;
    printf("0x%p\n", &Parent::add);
    cout << "virtual member function addree:" << endl;
    //虚成员函数
    printf("%d\n", &Parent::print);//1
    printf("%d\n", &Parent::sayHello);//5
    printf("%d\n", &Parent::func);//9

    return 0;
}
