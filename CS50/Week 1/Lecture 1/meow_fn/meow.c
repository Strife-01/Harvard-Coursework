#include <cs50.h>
#include <stdio.h>

void meow(int nr_of_times)
{
    for (int iterator = 0; iterator < nr_of_times; iterator++)
    {
        printf("meow\n");
    }
}

int main(void)
{
    int nr_of_meows = get_int("How many meows? ");
    meow(nr_of_meows);

    return 0;
}