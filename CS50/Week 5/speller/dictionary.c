// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// TODO: Choose number of buckets in hash table
#ifndef N
#define N 26
#endif

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash table
node *table[N];

// Loaded ? 
bool is_loaded = false;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Lowercase a copy of the word
    int len = strlen(word);
    char *copy = malloc(sizeof(char) * len + 1);
    strcpy(copy, word);

    for (int i = 0; i < len; i++)
    {
        copy[i] = tolower(copy[i]);
    }

    // Hash the copy
    int index = hash(copy);

    // Jump to the bucket where the word should be
    // Parse the list
    for (node *ptr = table[index]; ptr->next != NULL; ptr = ptr->next)
    {
        // If found return true
        if (strcmp(copy, ptr->word) == 0)
        {
            free(copy);
            return true;
        }
    }

    // If not found return false
    free(copy);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    // Initialize the Hash Table
    for (int i = 0; i < N; i++)
    {
        table[i] = malloc(sizeof(node));
        if (table[i] == NULL)
        {
            return false;
        }
        table[i]->next = NULL;
    }

    // Parse each string (lowercased) in the dictionary
    char character;
    char word[LENGTH + 1];
    int index = 0;
    while (fread(&character, 1, 1, dict))
    {
        if (character != '\n')
        {
            word[index] = character;
            index++;
        }
        else
        {
            word[index] = '\0';
            index = 0;
            
            // Get the hash location
            int pos = hash(word);
            node *w = malloc(sizeof(node));
            if (w == NULL)
            {
                return false;
            }

            // Add the string in the hash table
            strcpy(w->word, word);
            w->next = table[pos];
            table[pos] = w;
        }
    }

    // When the dictionary has been loaded
    is_loaded = true;
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (is_loaded == false) 
    {
        return 0;
    }
    else
    {
        int size = 0;

        for (int i = 0; i < N; i++)
        {
            for (node *ptr = table[i]; ptr->next != NULL; ptr = ptr->next)
            {
                size++;
            }
        }
        return size;
    }
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Unloads all the elements in the dict 
    // Parse the dictionary
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];
        while (ptr->next != NULL)
        {
            node *copy = ptr->next;
            free(ptr);
            ptr = copy;
        }
        free(ptr);
    }
    return true;
}
