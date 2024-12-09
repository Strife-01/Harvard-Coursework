#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask the user how many meows they want 
    int counter = get_int("How many times to meow? ");

    // while from max till min
    // // use while to print meow counter nr of times
    // while (counter > 0)
    // {
    //     // print meow
    //     printf("meow\n");
    //     // decrement the counter 
    //     counter--;
    // } 

    // // make the counting from 0 (be careful at off by 1)
    // int iterator = 0;

    // while (iterator < counter)
    // {
    //     printf("meow\n");
    //     iterator++;
    // }

    // // use the for loop
    // for (int iterator = 0; iterator < counter; iterator++)
    // {
    //     printf("meow\n");
    // }

    // forever loop
    while (1)
    {
        printf("meow\n");
    }
}