#include <stdio.h>

void bubble_sort(int arr[], int length);
void swap(int *a, int *b);

int main(void)
{
	// Declare a test unsorted array of ints
	int arr[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};
	int length = sizeof(arr) / sizeof(arr[0]);

	// Sort the array
	bubble_sort(arr, length);

	// Print the sorted array
	for (int i = 0; i < length; i++)
	{
		printf("%i ", arr[i]);
	}
	printf("\n");
}

void bubble_sort(int arr[], int length)
{
	int swaps = length;

	while (swaps > 0)
	{
		swaps = 0;

		for (int i = 0; i < length - 1; i++)
		{
			if (arr[i] > arr[i + 1])
			{
				swap(&arr[i], &arr[i + 1]);
				swaps++;
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