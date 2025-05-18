#include <stdio.h>
#include <stdlib.h>
void __attribute__ ((constructor)) premain()
{
    printf("$ ");
}
int main(void)
{
    
    char *lptr = NULL;
    size_t len; 
    ssize_t read = getline(&lptr, &len, stdin);
    if(read != -1)
    {
        printf("%s", lptr);
    }
    free(lptr);
}