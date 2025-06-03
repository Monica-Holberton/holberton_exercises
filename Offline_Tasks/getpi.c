#include <stdio.h>
#include <unistd.h>

/**
 * main - PID
 *
 * Return: Always 0.
 */
int main(void)
{
    pid_t my_pid;
    pid_t parent;
    my_pid = getpid();
    parent = getppid();
    printf("%u\n", my_pid);
    printf("%u\n", parent);
    return (0);
}