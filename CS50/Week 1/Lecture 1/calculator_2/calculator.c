#include <stdio.h>

int main(void)
{
    const int x = 1;
    const int y = 3;

    // using type casting to eliminate truncation
    float z = (float) x / (float) y;

    printf("%f\n", z);
}

// integer overflow - when counting too high and running out of memory (bits)
// floating point imprecision 