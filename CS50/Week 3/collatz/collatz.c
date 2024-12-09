#include <cs50.h>
#include <stdio.h>

int collatz(int n);

int main(void)
{
	int number = get_int("enter a number: ");
	int answer = collatz(number);

	printf("to get to 1 you need %i steps.\n", answer);

	return 0;
}

int collatz(int n)
{
	if (n == 1)
	{
		return 0;
	}
	else
	{
		if (n % 2 == 0)
		{
			
			return 1 + collatz(n / 2);
		}
		else
		{
			return 1 + collatz(3 * n + 1);
		}
	}
}
