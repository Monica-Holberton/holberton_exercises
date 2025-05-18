#include <stdio.h>
void __attribute__ ((constructor)) premain(void)
{
    printf("before main()\n");
}
int main(void)
{
    return (0);
}