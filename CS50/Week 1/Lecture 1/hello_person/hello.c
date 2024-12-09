#include "cs50.h"
#include <stdio.h>

int main(void)
{
    // Ask for person's name
    string name = get_string("What is your name? ");
    // Greet the person
    printf("Hello, %s!\n", name);

    return 0;
}