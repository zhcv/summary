#include <iostream>
#include <limits>

int main(int argc, char *argv[])
{
	 using namespace std;

	 if ( argc != 3 )  // argc should be 2 for correct execution
         {
              // We print argv[0] assuming it is the program name
		 cout << "usage: " << argv[0] << " <filename> <option>\n ";
	 }
	 else
	 {
		 cout << argv[1] << " - argv[1]" << endl;
		 cout << argv[2] << " - argv[2]" << endl;
	 }

	cout << "Press ENTER to continue...";
	cin.ignore(numeric_limits<streamsize>::max(), '\n' );
	return 0;

}
