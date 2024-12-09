#include "cs50.h"
#include <stdio.h>

int main(void)
{
    // ask the user for x
    int x = get_int("X = ");
    // ask the user for y
    int y = get_int("Y = ");
    // check if x > y
    if (x > y)
    {
        // if so print
        printf("X is greater than Y\n");
    }
    // else check if x < y
    else if (x < y)
    {
        // if so print
        printf("X is less than Y\n");
    }
    // else
    else 
    {
        // print equality
        printf("X is equal to Y\n");
    }
    
    return 0;
}