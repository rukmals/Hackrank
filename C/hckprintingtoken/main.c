#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s[1001];
    fgets(s,1001,stdin);
    for(int i=0;i<strlen(s);i++){
        if(s[i]==' '){
            printf("\n");
        }
        else{
            printf("%c",s[i]);
        }
    }
    return 0;
}
