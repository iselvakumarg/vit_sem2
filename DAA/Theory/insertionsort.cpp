#include <math.h>
#include <stdio.h>
#include<ctime>
/* Function to sort an array 
   using insertion sort*/
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) 
    {
        key = arr[i];
        j = i - 1;
  
        /* Move elements of arr[0..i-1], 
           that are greater than key, 
           to one position ahead of 
           their current position */
        while (j >= 0 && arr[j] > key) 
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
  
// A utility function to print 
// an array of size n
void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
  
// Driver code
int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
  	clock_t tStart = clock();
    insertionSort(arr, n);
    	//  number of clock ticks elapsed since an epoch related to the particular program execution
	// divide by CLOCKS_PER_SEC to get number of seconds taken
	double time1=(double)(clock() - tStart)/CLOCKS_PER_SEC;
	printf("%f", time1);
    printArray(arr, n);
  
    return 0;
}
