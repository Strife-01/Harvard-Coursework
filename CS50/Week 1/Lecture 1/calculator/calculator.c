#include <cs50.h>
#include <stdio.h>

float add(float x, float y)
{
    return x + y;
}

int main(void)
{
    float x = get_int("x = ");
    float y = get_int("y = ");

    printf("%.2f\n", add(x, y));

    return 0;
}