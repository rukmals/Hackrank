while 1:
    arr_0= list(map(int,raw_input().strip().split(' ')))
    n=arr_0[0]
    k=arr_0[1]
    arr = list(map(int,raw_input().strip().split(' ')))
    count = 0
    if 2<=n<=100 and 1<=k<=100:
        for i in range(len(arr)):
            x=arr[i]
            if 1<=x<=100:
                for j in range(i+1,len(arr)):
                    y=x+arr[j]
                    if y%k==0:
                        count+=1
        print count
                    
                
            
