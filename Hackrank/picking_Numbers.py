n=input()
if 2<=n<=100:
    a=list(map(int,raw_input().strip().split()))
    a.sort()
    b=[]
    for i in range(len(a)):
        if 0<a[i]<100:
            y=[]
            y.append(a[i])
            for j in range(i+1,len(a)):
                x=abs(a[i]-a[j])
                if x<=1:
                    y.append(a[j])
            if len(y)>=2:
                b.append(len(y))
    print max(b)    
                
                
            
