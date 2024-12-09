#include <stdio.h>
#include "merge_sort.h"

// Function declarations

// int main(void)
// {
//     // Declare a test unsorted array of ints
//     int arr[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};

//     // Get it's length
//     unsigned int length = sizeof(arr) / sizeof(arr[0]);
//     int index = 0;

//     // Declare where to start sorting from
//     unsigned int start = 0;
//     unsigned int stop = length - 1;

//     // Sort the array
//     merge_sort(arr, start, stop);

//     // Print the sorted array
//     for (index = 0; index < length; index++)
//     {
//         printf("%i ", arr[index]);
//     }
//     printf("\n");

// }

void merge_sort(int arr[], unsigned int start, unsigned int stop)
{
    // Check if there is only one element in the array and exit if so
    // If only one element inside the array it means that it is sorted by default
    if (start >= stop)
    {
        return;
    }

    // Split the problem in two halfs and sort the two halfs
    // If there are more than one elements in the arrays it means that it can have unsorted elements
    unsigned int mid = start + (stop - start) / 2;

    // Merge left half
    merge_sort(arr, start, mid);

    // Merge the right half
    merge_sort(arr, mid + 1, stop);

    // Merge the two halfs together
    merge(arr, start, mid, stop);
}

void merge(int arr[], unsigned int start, unsigned int mid, unsigned int stop)
{
    // Get the lengths of the two buffer arrays for the left and right halfs elements
    unsigned int left_array_size = mid - start + 1;
    unsigned int right_array_size = stop - mid;

    int i = 0;
    int j = 0;
    int k = start;

    // Create the temporary arrays
    int left_arr[left_array_size];
    int right_arr[right_array_size];

    // Populate the arrays with their elements

    for (i = 0; i < left_array_size; i++)
    {
        left_arr[i] = arr[start + i];
    }
    for (j = 0; j < right_array_size; j++)
    {
        right_arr[j] = arr[mid + 1 + j];
    }

    // Update the initial array with the elements in the sorted order
    i = 0;
    j = 0;

    while (i < left_array_size && j < right_array_size)
    {
        if (left_arr[i] <= right_arr[j])
        {
            arr[k] = left_arr[i];
            i++;
        }
        else
        {
            arr[k] = right_arr[j];
            j++;
        }

        k++;
    }

    // Add the remaining elements from the left array if any
    while (i < left_array_size)
    {
        arr[k] = left_arr[i];
        i++;
        k++;
    }

    // Add the remaining elements from the right array if any
    while (j < right_array_size)
    {
        arr[k] = right_arr[j];
        j++;
        k++;
    }
}