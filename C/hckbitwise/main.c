#include <stdio.h>
#include <stdlib.h>

int main()
{
    printf("Hello world!\n");
    int n;
    int y;
    /*int *pn = &n;*/
    scanf("%d%d",&n,&y);
    int arr[n];
    for(int i=0;i<=n;i++){
        arr[i]=i+1;

    }
    int maxand[n*n];
    int count=0;
    int count1=0;
    int count2=0;
    int maxor[n*n];
    int maxxor[n*n];
    for(int j=0;j<n;j++){
        int a=0;
        for(int k=j+1;k<n;k++){
            /*printf("%d%d\n",arr[j],arr[k]);*/
            int and = arr[j]&arr[k];
            /*printf("%d",and);*/
            int or = arr[j]|arr[k];
            int xor = arr[j]^arr[k];
            if(and<y){

                maxand[count]=and;
                count++;
            }
            if(or<y){
               /* printf("%d\n",or);*/
               maxor[count1] = or;
               count1++;
            }
            if(xor<y){
               maxxor[count2] = xor;
               count2++;
            }

        }
    }
    int maxa=maxand[0];
    for(int x=0;x<count;x++){
        /*printf("%d\n",maxand[x]);*/
        if(maxand[x]>maxa){
            maxa=maxand[x];
        }
    }
    printf("%d\n",maxa);
    int maxo=maxor[0];
    for(int x1=0;x1<count1;x1++){

        if(maxo<maxor[x1]){
            maxo=maxor[x1];
        }
    }
    printf("%d\n",maxo);
    int maxx=maxxor[0];
    for(int x2=0;x2<count2;x2++){
        if(maxxor[x2]>maxx){
            maxx=maxxor[x2];
        }
    }
    printf("%d\n",maxx);

    /*int arr[5]={1,2,5,3,10};
    int a,b;

    for(int y=0;y<25;y++){
        if(arr[y]>max){
            max=arr[y];
        }
    }
    printf("%d",max);*/
    return 0;
}

