#include <cs50.h>
#include <ctype.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#ifndef MAX
#define MAX 9
#endif

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Parse the candidate array to look for the specific candidate
    for (size_t i = 0; i < candidate_count; i++)
    {
        // If the candidate is inside the candidate array return true (it is case sensitive)
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // set the innitial winner to candidate 0
    int max_votes = candidates[0].votes;

    // Parse the candidates array and get the max number of votes
    for (size_t i = 1; i < candidate_count; i++)
    {
        // check for winner
        if (max_votes < candidates[i].votes)
        {
            max_votes = candidates[i].votes;
        }
    }

    // Print the winner/s
    for (size_t i = 0; i < candidate_count; i++)
    {
        // if the candidate has the max number of votes print
        if (candidates[i].votes == max_votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }

    return;
}