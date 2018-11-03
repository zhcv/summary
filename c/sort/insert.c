#include <stdio.h>

void insertSort(int A[], int n){
    for (int i=1; i<n; i++)
    {
	int get = A[i];
	int j = i - 1;
	while (j >= 0 && A[j] > get)
	{
	    A[j+1] = A[j];
	    j--;
	}

        A[j+1] = get; 
    }
}

int main()
{
    int a[] = {6,5,3,1,8,7,1,2};
    int n = sizeof(a) / sizeof(int);
    printf("排序前序列:\n");
    for (int i=0; i<n; i++)
    {
	printf("%d ", a[i]);
    }
    printf("\n排序后序列:\n");
    insertSort(a, n);

    for (int i=0; i<n; i++)
    {
	printf("%d ", a[i]);
    }
    printf("\n");

}
