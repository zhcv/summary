#include "header.h"
#include "functions.c"

int main() {
	int n;		// Number of operations to be performed. Input taken : 1 Million
	DynamicTable *tbl;
	printf("Enter the number of operations you want to perform:  ");
	scanf("%d",&n);
	printf("All time measurements are in milliseconds\n");
	int ratio;	// Ratio of inserts to deletes
	for(ratio = 0; ratio < 3; ratio++) {
		row = 0;		// The row number in the matrix timeStats
		int i = 0;		// To keep track of size increment factor
		int d = 0;		// To keep track of size decrement factor
		double incrementArr[] = {2, 3, 1.75, 1.5, 1.25};	// Factors considered for resizing array after insertion 
		double decrementArr[] = {0.25, 0.5, 0.75};			// Factors considered for resizing array after deletion
		switch(ratio) {
			case 0: printf("\nRatio of inserts and deletes: 1:1\n"); break;	
			case 1: printf("\nRatio of inserts and deletes: 3:2\n"); break;
			case 2: printf("\nRatio of inserts and deletes: 4:2\n"); break;
		}
		// Printing the header for the matrix timeStats
		printf("Increment Factor\tDecrement Factor\tMax Insertion Time\tMax Deletion Time\tAverage of all\tAverage of Inserts\tAverage of Deletes\n");
		for( i = 0; i < 5; i++) {
			for( d = 0; d < 3; d++) {
		//while(row < 5)  {			
			timeStats[row][0] = incrementArr[i];
			timeStats[row][1] = decrementArr[d];
	 		tbl = initDynamicTable(tbl, incrementArr[i], decrementArr[d]);		// Initialising a pointer to the Dynamic Table structure
			performOperations(tbl, n, ratio);			// Calls insert and deletion functions 
			row++;
			}
		
		}
		for(int i = 0; i < 15; i++) {
			for(int j = 0; j < 7; j++) {
				printf("%lf\t\t", timeStats[i][j]);
			}
			printf("\n");
		}
		free(tbl->arr);
		free(tbl);	
	}
	return 0;
}

