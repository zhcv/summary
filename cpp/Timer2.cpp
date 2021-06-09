 #include <iostream>
 #include <chrono>
 
 using namespace std;
 
 int main(){
     cout << "system_clock" << endl;
     cout << chrono::system_clock::period::num << endl;
     cout << chrono::system_clock::period::den << endl;
     cout << "steady = " << boolalpha << chrono::system_clock::is_steady << endl << endl;
 
     cout << "high_resolution_clock" << endl;
     cout << chrono::high_resolution_clock::period::num << endl;
     cout << chrono::high_resolution_clock::period::den << endl;
     cout << "steady = " << boolalpha << chrono::high_resolution_clock::is_steady << endl << endl;
 
     cout << "steady_clock" << endl;
     cout << chrono::steady_clock::period::num << endl;
     cout << chrono::steady_clock::period::den << endl;
     cout << "steady = " << boolalpha << chrono::steady_clock::is_steady << endl << endl;
 
     return 0;
}


/* ***************************************************************************
 auto start = chrono::steady_clock::now();
 
 //
 //  Insert the code that will be timed
 //
 
 auto end = chrono::steady_clock::now();
  
 // Store the time difference between start and end
 auto diff = end - start;

 // 如果你想要打印start和end的差值，你可以使用：
 cout << chrono::duration <double, milli> (diff).count() << " ms" << endl;

 // 如果你更喜欢纳秒，你使用：
 cout << chrono::duration <double, nano> (diff).count() << " ns" << endl;

  // diff以被截断成整数，结果如下：
 diff_sec = chrono::duration_cast<chrono::nanoseconds>(diff);
  cout << diff_sec.count() << endl;

 *************************************************************************** */
