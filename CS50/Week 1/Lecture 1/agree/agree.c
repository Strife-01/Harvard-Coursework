#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask the user if they agree and store the answer in a char
    char answer;
    
    // check to see if the user introduced the correct input
    do
    {
        answer = get_char("Do you agree? [Y/N]: ");
    }
    while (
    answer != 'y' 
    && answer != 'Y'
    && answer != 'n' 
    && answer != 'N'
    );

    // check if the user's answer is positive
    if (answer == 'Y' || answer == 'y')
    {
        // let the user know it is positive
        printf("You agree!\n");
    }
    // if not let them know they disagree
    else
    {
        printf("You disagree!\n");
    }

    return 0;
}