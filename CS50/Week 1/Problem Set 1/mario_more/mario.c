#include <cs50.h>
#include <stdio.h>

int main (void)
{
	int dimensions;

	do 
	{
		dimensions = get_int("Height: ");
	}
	while (dimensions < 1);

	const int height = dimensions;
	const int width = dimensions * 2 + 2;
	int first_half_parse = width / 2 - 2;
	int second_half_parse = width / 2 + 2;

	for (int i = 0; i < height; i++)
	{
		for (int j = 0; j < width; j++)
		{
			if (j <= width / 2 - 2)
			{
				if (j < first_half_parse)
				{
					printf(" ");
				}
				else
				{
					printf("#");
				}
			}
			else if (j > width / 2 - 2 && j < width / 2 + 1)
			{
				printf(" ");
			}
			else 
			{
				if (j < second_half_parse)
				{
					printf("#");
				}
				else
				{
					printf(" ");
				}

			}


		}
		first_half_parse--;
		second_half_parse++;
		printf("\n");
	}
	return 0;

}
