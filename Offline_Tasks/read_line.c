#include <stdio.h>
#include <unistd.h>

int main(int ac, char **av)
{
        char *usr_line = NULL;
        size_t *n = 0;
        ssize_t my_func;

        while(1)
        {
                printf("$ ");
                my_func = getline(&usr_line, &n, stdin);

                if (my_func == -1)
                {
                        break;
                }
                printf("%s\n", line);
        }
        return 0;
}