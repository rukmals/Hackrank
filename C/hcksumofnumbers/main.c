#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d",&n);
    int sum=0;
    for(int i=0;i<=4;i++){
        sum=sum+n%10;
        n=n/10;

    }
    printf("%d",sum);
    return 0;
}
