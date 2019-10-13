#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j ;
    int rows ;
    scanf("%d",&rows);
    for(i=rows; i>=1; --i)
    {
        for(int space=0; space < rows-i; ++space)
            printf("%d ",rows-space);
        for(j=1; j<=i; ++j)
            printf("%d ",i);
        for(j=1; j<=i-1; ++j)
            printf("%d ",i);
        for(int space=0; space <rows-i; space++)
            printf("%d ",space+i+1);
        printf("\n");

    }
    for(i=rows; i>1; --i)
    {
        for(j=2; j<=i; ++j)
            printf("%d ",rows-j+2);
        for(j=1; j<=rows-i+1; ++j)
            printf("%d ",rows-i+2);
        for(j=1; j<=rows-i+1; ++j)
            printf("%d ",rows-i+2);
        for (int x=i-2;x>=1;--x)
            printf("%d ", i-x+rows-i+1);




        printf("\n");

    }

    return 0;
}
