#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int a[100];//100个元素的整型数组。
    int i;
    for(i = 0; i < 100; i ++)//输入元素。
        // cin>>a[i];
        a[i] = i;
         
    ofstream f("out.txt");//打开out.txt文件。
    for(i = 0; i < 100; i ++)//写入到文件。
        f << a[i] << endl; //写入每个元素，每个元素单独一行。
    return 0;
}
