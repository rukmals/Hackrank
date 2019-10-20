#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr;
    int limit=5;
    ptr = (int*)malloc(limit*sizeof(int));
    ptr[0]=1;
    ptr[1]=2;
    ptr[2]=3;
    int n=3;
    for(int i=0;i<2;i++){
        ptr[n+i]=ptr[i]+ptr[i+1]+ptr[i+2];
    }
    printf("%d",ptr[4]);
    return 0;
}
