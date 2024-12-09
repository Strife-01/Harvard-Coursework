#include "merge_sort.h"
#include <stdbool.h>
#include <stdio.h>

bool binary_search(int searched, int *arr, unsigned int left, unsigned int right);

int main(void)
{
    int arr_test[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};
    int length = sizeof(arr_test) / sizeof(arr_test[0]);
    int searched = 0;
    
    printf("Searched number is: \n");
    scanf("%i", &searched);

    merge_sort(arr_test, 0, length - 1);

    if (binary_search(searched, arr_test, 0, length - 1))
    {
        printf("The number %i is inside the array\n", searched);
    }
    else
    {
        printf("The number %i cannot be found inside the array\n", searched);
    }

    return 0;
}

bool binary_search(int searched, int *arr, unsigned int left, unsigned int right)
{
    if (left > right)
    {
        return false;
    }

    int mid = left + (right - left) / 2;

    if (arr[mid] > searched)
    {
        return binary_search(searched, arr, left, mid - 1);
    }
    else if (arr[mid] < searched) 
    {
        return binary_search(searched, arr, mid + 1, right);
    }
    else 
    {
        return true;
    }
}