#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age = 20;
    int *pAge = &age;
    printf("age's memory address: %p",&pAge);
    return 0;
}
