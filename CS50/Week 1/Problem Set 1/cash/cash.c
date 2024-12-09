#include <cs50.h>
#include <stdio.h>

const int penny = 1;
const int nickel = 5;
const int dime = 10;
const int quarter = 25;

int how_many_quarter (int remaining)
{
	return remaining / quarter;
}

int how_many_dime (int remaining)
{
	return remaining / dime;
}

int how_many_nickel (int remaining)
{
	return remaining / nickel;
}

int how_many_penny (int remaining)
{
	return remaining / penny;
}

int main(void)
{
	int change;
	int nr_of_coins = 0;

	do
	{
		change = get_int("Change owed: ");
	}
	while (change < 0);

	if (change == 0)
	{
		printf("0\n");
		return 0;
	}

	int quarter_owed = how_many_quarter(change);
	change -= quarter_owed * quarter;
	int dime_owed = how_many_dime(change);
	change -= dime_owed * dime;
	int nickel_owed = how_many_nickel(change);
	change -= nickel_owed * nickel;
	int penny_owed = how_many_penny(change);

	nr_of_coins = quarter_owed + dime_owed + nickel_owed + penny_owed;

	printf("%i\n", nr_of_coins);

	return 0;
}
