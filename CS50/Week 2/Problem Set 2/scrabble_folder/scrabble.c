#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#ifndef NUMBER_LETTERS

#define NUMBER_LETTERS 26
const int letter_scores[NUMBER_LETTERS] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

#endif

int main(void)
{
	// prompt players for answers
	string player_1 = get_string("Player 1? ");
	string player_2 = get_string("Player 2? ");

	// declare the scores
	int score_p1 = 0;
	int score_p2 = 0;

	// compute the scores
	int length_1 = strlen(player_1);
	int length_2 = strlen(player_2);

	int max_length = length_1 >= length_2? length_1: length_2;
	
	
	for (int letter = 0; letter < max_length; letter++)
	{
		if (letter < length_1)
		{
			score_p1 += letter_scores[toupper(player_1[letter]) - 65];
		}

		if (letter < length_2)
		{
			score_p2 += letter_scores[toupper(player_2[letter]) - 65];
		}
	}

	if (score_p1 > score_p2)
	{
		printf("Player 1 wins!\n");
	}
	else if (score_p1 < score_p2)
	{
		printf("Player 2 wins!\n");
	}
	else
	{
		printf("Tie!\n");
	}

	return 0;

}
