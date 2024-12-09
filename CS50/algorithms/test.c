#include <stdio.h>

int main(void)
{
	char *x[2];
	x[0] = "Hi!";
	x[1] = "Bye!";
	printf("%s %s\n", x[0], x[1]);
}

