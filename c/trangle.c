#include <stdio.h>

/* Program to calculate the area of a triangle */

int main(void)
{
    float area;   	// declare float variable area
    float height, base; // declare more float variables
    int sides=3; 	// declare and initialize integer
    			// variable
    height=2.5; 		// assign number 2.5 to height
    base=3.5; 			// assign number 3.5 to base
    area=0.5*height*base; 	// calculate the product
    				// 0.5*height*base
    				// and assign it to variable area
    				// print a message with the result
    printf("The area of this shape with %d sides ", sides);
    printf("is %f\n", area);
    return 0;
}
