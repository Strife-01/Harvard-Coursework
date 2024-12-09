#include <stdio.h>

void selection_sort(int arr[], int length);
void swap(int *a, int *b);

int main(void)
{
    // Declare a test unsorted array of ints
	int arr[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};
	int length = sizeof(arr) / sizeof(arr[0]);

    // Sort the array using selection sort algorithm
    selection_sort(arr, length);

    // Print array
    for (int i = 0; i < length; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
}

void selection_sort(int arr[], int length)
{
    for (int i = 0; i < length - 1; i++)
    {
        for (int j = i + 1; j < length; j++)
        {
            if (arr[j] < arr[i])
            {
                swap(&arr[i], &arr[j]);
            }
        }
    }
}

void swap(int *a, int *b)
{
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}