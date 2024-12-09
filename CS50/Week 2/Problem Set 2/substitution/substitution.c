#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#ifndef NR_CHARACTERS

#define NR_CHARACTERS 26
int frequency_letters[NR_CHARACTERS];

#endif

int main(int argc, string argv[])
{
    // check for the number of cla
    if (argc != 2)
    {
        printf("Usage ./substitution KEY\n");
        return 1;
    }

    // check for the correctness of the key
    int length = strlen(argv[1]);
    if (length != 26)
    {
        printf("Usage ./substitution KEY\n");
        return 2;
    }

    // reset frequency array
    for (int i = 0; i < NR_CHARACTERS; i++)
    {
        frequency_letters[i] = 0;
    }

    for (int i = 0; i < length; i++)
    {
        frequency_letters[tolower(argv[1][i] - 97)]++;
        if (frequency_letters[tolower(argv[1][i] - 97)] > 1)
        {
            printf("Usage ./substitution KEY\n");
            return 3;
        }
    }

    // prompt the user for text
    string plaintext = get_string("plaintext:  ");

    // iterate it and show the ciphertext
    length =  strlen(plaintext);
    printf("ciphertext: ");
    for (int i = 0; i < length; i++)
    {
        if (isupper(plaintext[i]))
        {
            printf("%c", toupper(argv[1][plaintext[i] - 65]));
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", tolower(argv[1][plaintext[i] - 97]));
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}