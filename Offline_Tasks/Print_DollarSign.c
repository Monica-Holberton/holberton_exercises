#include <stdio.h>
#include <stdlib.h>

/**
 * print_prompt - prints the shell prompt before main runs
 */
void __attribute__((constructor)) print_prompt(void)
{
	printf("$ ");
}

/**
 * main - Entry point of the shell
 * Return: 0
 */
int main(void)
{
	char *line = NULL;
	size_t size = 0;
	ssize_t nread;

	while ((nread = getline(&line, &size, stdin)) != -1)
	{
		printf("%s", line);
	}
	free(line);
	return (0);
}
