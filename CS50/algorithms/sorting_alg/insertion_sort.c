
#include "merge_sort.h"
#include <stdio.h>
#include <stdlib.h>

#define START_LENGTH 19

int main()
{
    // Declare a test unsorted array of ints
    int length = START_LENGTH;
	int *arr = malloc(sizeof(int) * length);

    int arr_test[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};
    arr = arr_test;

    // Sort the array
    int start = 0;
    int stop = length - 1;

    // printf("%i\n", length);

    merge_sort(arr, start, stop);

    // Print sorted array
    for (int i = 0; i < length; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");

    // Get user input and sort the array on the go (listen until 0 or no valid number)
    int new_num;
    while (scanf("%i", &new_num) && new_num != 0)
    {
        // Search array to find index where the number should be
        int left = 0;
        int right = length - 1;
        int position = 0;
        int last_index_visited = 0;

        // Get the overall location where the new element should be
        while(left <= right)
        {
            int mid = left + (right - left) / 2;
            last_index_visited = mid;

            if (new_num < arr[mid])
            {
                right = mid - 1;
            }
            else if (new_num > arr[mid])
            {
                left = mid + 1;
            }
            else
            {
                break;
            }
        }

        // Pinpoint the exact location where the element needs to be inserted
        if (new_num == arr[last_index_visited])
        {
            position = last_index_visited;
        }
        else if (new_num < arr[last_index_visited])
        {
            position = last_index_visited;
        }
        else
        {
            position = last_index_visited + 1;
        }

        // Buffer arrays lengths
        int elements_on_right = length - position;
        int elements_on_left = length - elements_on_right;

        // Buffer arrays
        int buffer_array_right[elements_on_right];
        int buffer_array_left[elements_on_left];

        printf("%i\n", elements_on_right);

        // Copy elements in buffers
        // Elements on the right of the position
        for (int i = 0;i < elements_on_left; i++)
        {
            buffer_array_left[i] = arr[i];
        }

        // Elements from the position onwards
        for (int j = 0; j < elements_on_right; j++)
        {
            buffer_array_right[j] = arr[position + j];
        }

        // Update length
        length++;

        // Create the new array
        int *new_arr = malloc(sizeof(int) * length);

        // Elements before the inserted element
        for (int i = 0; i < elements_on_left; i++)
        {
            new_arr[i] = buffer_array_left[i];
        }

        // The inserted element at its position
        new_arr[position] = new_num;

        // Elements after the inserted element
        for (int i = 0; i < elements_on_right; i++)
        {
            new_arr[position + 1 + i] = buffer_array_right[i];
        }

        // Replace the old array with the new one
        arr = new_arr;
    }

    // Print new sorted array
    for (int i = 0; i < length; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");

    // Free the allocated memory when you are done with it
    free(arr);
}