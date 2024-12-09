#include <cs50.h>
#include <stdio.h>

// #define DIMENSION 8

int main(void)
{
	/*
	int height = DIMENSION;
	int width = DIMENSION;
	int solid_steps = width - 1;
	*/
	int dimensions;

	do
	{
		dimensions = get_int("Height: ");
	}
	while (dimensions < 1);

	const int height = dimensions;
	const int width = dimensions;
	int solid_steps = width - 1;

	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			if (solid_steps > j)
			{
				printf(" ");
			}
			else
			{
				printf("#");
			}

		}
		solid_steps--;
		printf("\n");
	}

	return 0;
}
