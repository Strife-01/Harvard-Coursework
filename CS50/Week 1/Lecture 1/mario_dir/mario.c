#include <cs50.h>
#include <stdio.h>

// #ifndef ROW

// #define ROW 4

// #endif

// #ifdef ROW

// #define COLUMN 5

// #endif

int main(void)
{
    int n;

    do 
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    for (size_t i = 0; i < n; i++) 
    {
        for (size_t j = 0; j < n; j++) {
        printf("#");
        }
    printf("\n");
    }

    return 0;
}