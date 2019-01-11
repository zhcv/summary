#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

#ifndef STRUCT_H
#define STRUCT_H
typedef struct dynamictable {
	int *arr;
	int maxSize;
	int currentSize;
	double incr;
	double dec;
} DynamicTable;
#endif

DynamicTable *initDynamicTable(DynamicTable *tbl, double incr, double dec);
void performOperations(DynamicTable *tbl, int n, int ratio);
void insert(DynamicTable *tbl, int ele);
int deletion(DynamicTable *tbl);
void computeStats(DynamicTable *tbl, double *insertTime, double *deletionTime, int ins, int del);
double max(double *arr, int size);
double sum(double *arr, int size);
void copy(int *copyFrom, int *copyTo, int n); 
double time_elapsed(struct timespec *start, struct timespec *end);
//void printDynamicTable(DynamicTable *tbl);
double timeStats[15][7];
int row = 0;



