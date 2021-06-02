#include <iostream>
#include <string>

// g++ -std=c++11 getline_push.cpp -o get
// g++ -std=c++0x your_file.cpp -o your_program

using namespace std;

int main() 
{
    // Declaring string
    string str;
    // Taking string input using getline()
    // "geeksforgeeks" in givin output
    getline(cin, str);

    // Displaying string
    cout << "The initial string is :";
    cout << str << endl;
    

    // Using push_back() to insert a character
    // at end
    // putshes 's' in this case
    str.push_back('s');
    
    // Displaying string 
    cout << "The string after push_back operation is : ";
    cout << str << endl;
 

    
    // Using pop_pack() to delete a character
    // from end
    // pops 's' in this case
    str.pop_back();

    // Displaying string
    cout << "The string after pop_back operation is :";
    cout << str << endl;

    return 0;
}
