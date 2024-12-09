#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

bool isLegit(long card_number);
int getNumberOfDigits(long card_number);
long getPowerOf10(int nr_of_digits);

int main(void)
{
	long card_number = get_long("Number: ");

	if(isLegit(card_number) == false)
	{
		printf("INVALID\n");
		return 1;
	}

	int nr_digits = getNumberOfDigits(card_number);

	if (nr_digits == 15 && (card_number / getPowerOf10(13) == 34 || (card_number / getPowerOf10(13) == 37)))
	{
		printf("AMEX\n");
		return 0;
	}
	
	if (nr_digits == 16)
	{
		if (card_number / getPowerOf10(14) >= 51 && card_number / getPowerOf10(14) <= 55)
		{
			printf("MASTERCARD\n");
			return 0;
		}
		else if (card_number / getPowerOf10(15) == 4)
		{
			printf("VISA\n");
			return 0;
		}
	}

	if (nr_digits == 13 && (card_number / getPowerOf10(12) == 4))
	{
		printf("VISA\n");
		return 0;
	}

	printf("INVALID\n");
	return 1;
}

bool isLegit(long card_number)
{
	long n = card_number;
	int sum_1 = 0;
	int sum_2 = 0;
	int sum_total = 0;
	while (n)
	{
		int digit = n % 100 / 10;
		
		digit *= 2;	

		if (digit > 9)
		{
			digit = digit % 10 + 1;
		}
		sum_1 += digit;
		sum_2 += n % 10;
		n /= 100;
	}

	sum_total = sum_1 + sum_2;

	if (sum_total % 10 == 0)
	{
		return true;
	}
	return false;
}

int getNumberOfDigits(long card_number)
{
	int n = 0;

	while(card_number)
	{
		n++;
		card_number /=10;
	}

	return n;
}

long getPowerOf10(int nr_of_digits)
{
	long output = 1;

	for (int i = 0; i < nr_of_digits; i++)
	{
		output *= 10;
	}

	return output;
}
