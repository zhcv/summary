

DynamicTable *initDynamicTable(DynamicTable *tbl, double incr, double dec) {
	tbl = (DynamicTable *)malloc(sizeof(DynamicTable));
	tbl->arr = (int *)malloc(sizeof(int));	// Initialising array size to integer size
	tbl->maxSize = 1;						// Max capacity of the array
	tbl->currentSize = -1;					// Number of elements currently residing in the array
	tbl->incr = incr;						// Factor by which array capacity must be increased for insertion, when the array is full
	tbl->dec = dec;							// Factor at which array capacity must be decreased following a deletion
	return tbl;
}

void performOperations(DynamicTable *tbl, int n, int ratio) {
	int ele;																		// Element to be inserted or element returned after deletion
	int insertCount;																// Number of insert operations to be performed
	struct timespec start;															// Struct variable for time 
	struct timespec end;															
	if(ratio == 0) {																// Calculating number of insert operations based on the ratio
		insertCount = ceil(n/2);
	}
	else if(ratio == 1) {
		insertCount  = ceil(3 * (n/5));
	}
	else if(ratio == 2) {
		insertCount = ceil(4 * (n/6));
	}
	int ins = 0;																	// Counter for insertTime array
	int del = 0;																	// Counter for deletionTime array
	double *insertTime = (double *)malloc(sizeof(double)*insertCount);				
	double *deletionTime = (double *)malloc(sizeof(double)*(n-insertCount));
	srand(time(NULL));
	for(int i = 0; i < insertCount; i++, ins++) {
			ele = ((rand()%10000) + 0)/100;											// Generating a random value to be inserted
			clock_gettime(CLOCK_REALTIME, &start);
			insert(tbl, ele);
			clock_gettime(CLOCK_REALTIME, &end);
			insertTime[ins] = time_elapsed(&start,&end);							// Storing runtime for each insert operation
			
	}
	for(int i = insertCount; i < n; i++, del++) {
			clock_gettime(CLOCK_REALTIME, &start);
			ele = deletion(tbl);
			clock_gettime(CLOCK_REALTIME, &end);
			deletionTime[del] = time_elapsed(&start,&end);							// Storing runtime for each deletion operation
	}
	computeStats(tbl, insertTime, deletionTime, ins, del);							// Computing the required time statistics
	free(insertTime);
	free(deletionTime);	
}

void insert(DynamicTable *tbl, int ele) {
	if(tbl->maxSize == (tbl->currentSize+1)) {										// If max capacity of the table has been reached
		int newSize = ceil(tbl->incr * tbl->maxSize);								// Using the resize factor
		int *temp = (int *)malloc(sizeof(int)*(tbl->currentSize));		// Temporary array to prevent data loss due to failed malloc				
		copy(tbl->arr, temp, tbl->currentSize);
		free(tbl->arr);		
		tbl->arr = (int *)malloc(sizeof(int)*newSize);
		if(!(tbl->arr)) {															// In case malloc fails
			tbl->arr = (int *)malloc(sizeof(int)*(tbl->currentSize));
			copy(temp, tbl->arr, tbl->currentSize);
			free(temp);
			printf("Error in resizing array\n");
			return;
		}
		copy(temp, tbl->arr, tbl->currentSize);										// Copying the existing data back
		tbl->maxSize = newSize;														
		free(temp);
	}
	tbl->currentSize += 1;															
	tbl->arr[tbl->currentSize] = ele;												// Inserting new element
	return;
}

int deletion(DynamicTable *tbl) {
	int ele = -1;																				// Element that is deleted
	int curr = tbl->currentSize;
	if((curr) > -1) {																			// Table is not empty
		ele = tbl->arr[curr];
		curr -= 1;
		int newSize = ceil(tbl->maxSize * tbl->dec);											// Condition for resizing the array
		if((curr+1) <= newSize) { 
			tbl->arr = realloc(tbl->arr, sizeof(int)*newSize);
			tbl->maxSize =  newSize;
			tbl->currentSize = curr;
		}
	}
	return ele;
}

void copy(int *copyFrom, int *copyTo, int n) {													// Copying elements from first array to second array
	for(int i = 0; i < n; i++) {
		copyTo[i] = copyFrom[i];
	}
}

void computeStats(DynamicTable *tbl, double *insertTime, double *deletionTime, int ins, int del){
	timeStats[row][2] = max(insertTime, ins);							// Maximum insertion time
	timeStats[row][3] = max(deletionTime, del); 						// Maximum deletion time
	double insertSum = sum(insertTime, ins);							// Total insertion time
	double deletionSum = sum(deletionTime, del);						// Total deletion time
	timeStats[row][4] = (insertSum + deletionSum)/(ins+del);			// Average insertion and deletion time
	timeStats[row][5] = insertSum/ins;									// Average insertion time
	timeStats[row][6] = deletionSum/del;								// Average deletion time
}

double max(double *arr, int size) {										// Helper function to calculate max time
	double max = -1.0;
	for(int i = 0; i < size; i++) {
		if(arr[i] > max) {
			max = arr[i];
		}
	}
	return max;	
}

double sum(double *arr, int size) {										// Helper function to calculate total time taken
	double s = 0.0;
	for(int i = 0; i < size; i++) {
		s += arr[i];
	}
	return s;	
}

double time_elapsed(struct timespec *start, struct timespec *end) {		// Calculate the time elapsed between function call and termination
	double t = 0.0;
	t = (end->tv_sec - start->tv_sec) * 1000;
	t += (end->tv_nsec - start->tv_nsec) * 0.000001;
	return t;
}

/*
void printDynamicTable(DynamicTable *tbl) {
	printf("\n");	
	for(int i = 0; i <= tbl->currentSize; i++) {
		printf("%d ", tbl->arr[i]);
	}
}*/
