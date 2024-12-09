#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
	// ask the user for input
	
	string passage = get_string("Text: ");

	int nr_letters = 0;
	int nr_words = 0;
	int nr_sentences = 0;

	// compute nr of letters
	// compute nr of words
	// compute nr of sentences
	
	int passage_length = strlen(passage);

	for (int i = 0; i < passage_length; i++)
	{
		// if sentence increment
		if ((passage[i + 1] == '.' || passage[i + 1] == '?' || passage[i+1] == '!' || passage[i+1] == '\0') && (isalnum(passage[i]) || passage[i] == ' '))
		{
			nr_sentences++;
		}
		// if letter increment
		if (isalpha(passage[i]))
		{
			nr_letters++;
		}
		// if word increment
		if (passage[i] == ' ')
		{
			nr_words++;
		}
	}

	// count the last word which doesn't have a space after it
	nr_words++;

	// compute nr of average letters per 100 words
	// compute nr of average sentences per 100 words
	
	float L = (float) nr_letters * 100.0 / (float) nr_words;
	float S = (float) nr_sentences * 100.0 / (float) nr_words;

	// compute the index and print it
	float index = 0.0588 * L - 0.296 * S - 15.8;

	// round the index to its nearest whole number
	if (index - (int) index < 0.5)
	{
		index = (int) index;
	}
	else
	{
		index = (int) index + 1;
	}

	if (index < 1)
	{
		printf("Before Grade 1\n");
	}
	else if (index >= 16)
	{
		printf("Grade 16+\n");
	}
	else
	{
		printf("Grade %i\n", (int) index);
	}

	return 0;
}
