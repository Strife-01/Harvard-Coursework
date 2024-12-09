#include <stdio.h>

int main(void)
{
    int arr_test[] = {50 , 31 , 21 , 28 , 72 , 41 , 73 , 93 , 68 , 43 , 45 , 78 , 5 , 17 , 97 , 71 , 69 , 61 , 88};
    int length = sizeof(arr_test) / sizeof(arr_test[0]);
    int searched = 0;
    
    printf("Searched number is: \n");
    scanf("%i", &searched);

    for (int i = 0; i < length; i++)
    {
        if (arr_test[i] == searched)
        {
            printf("The number %i is inside the array the position %i\n", searched, i);
            return 0;
        }
    }

    printf("The number %i cannot be found inside the array\n", searched);
    return 0;
}