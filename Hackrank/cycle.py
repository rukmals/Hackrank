n=input()
#l=[0,1,4]
if 1<=n<=10:
    for i in range(n):
        cycle=input()
        H= 1
        if cycle==0:
            print H
        if cycle==1:
            print H*2
        if 1<cycle<=60:
            for j in range(1,cycle+1):
                if j%2!=0:
                    H=H*2
                else:
                    H=H+1
            print H
                    
