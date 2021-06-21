#include <iostream>
// #include <math.h>
#include <cmath>
#include <random>

using namespace std;

void uniform(const int count, const float min, const float max, float *r) 
{
	std::uniform_real_distribution<float> dis(min, nextafter(max, std::numeric_limits<float>::max()));
	for (int i = 0; i < count; i++) {
    	r[i] = 5.0f;
	}
}


int main(int argc, char* argv[])
{
	float min = 0.1f;
	float max = 2.1f;
    std::uniform_real_distribution<float> dis(min, nextafter(max, std::numeric_limits<float>::max())); 

    double x = 0.0, y = 1.0;

    double resultInDouble = nextafter(x,y);
    cout << "nextafter(x, y) = " << resultInDouble << endl;

    return 0;
}
