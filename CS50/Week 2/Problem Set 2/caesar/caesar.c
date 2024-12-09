#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef NR_CHARACTERS

#define NR_CHARACTERS 26
const char characters_array[NR_CHARACTERS] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

#endif

int main(int argc, string argv[])
{
    // check for the correct number of CLA
    if (argc != 2)
    {
        printf("./caesar KEY\n");
        return 1;
    }

    // check for the correctness of the CLA
    int length = strlen(argv[1]);
    for (int i = 0; i < length; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("./caesar NUMERIC_KEY\n");
            return 2;
        }
    }

    // compute the key
    int key = 0;
    int power_of_10 = 1;
    for (int i = 0; i < length; i++)
    {
        key = key * power_of_10 + (argv[1][i] - 48);
        power_of_10 *= 10;
    }

    // prompt the user for the message
    string plaintext = get_string("plaintext:  ");
    length = strlen(plaintext);

    // print the ciphered text
    printf("ciphertext: ");
    for (int i = 0; i < length; i++)
    {
        if (islower(plaintext[i]))
        {
            printf("%c", tolower(characters_array[(plaintext[i] - 97 + key) % NR_CHARACTERS]));
        }
        else if(isupper(plaintext[i]))
        {
            printf("%c", characters_array[(plaintext[i] - 65 + key) % NR_CHARACTERS]);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");

    return 0;
}