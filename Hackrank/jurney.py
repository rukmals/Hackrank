#F-
#A-aware from each station
#P-price
#U-unit of tank max
#k-bigin unit in tank
import sys
List = list(map(int,sys.stdin.readline().split()))
ch,n=List[0],List[1]
if 1<=ch<=1000 and 1<=n<=1000000:
    #List_=[[1,2],[1,3],[1,2]]
    List_=[]
    count=0
    for i in range(n):
        data =list(map(int,sys.stdin.readline().split()))
        List.append(data)
    data_1=list(map(int,sys.stdin.readline().split()))
    #data_1=[1,3,2]
    for j in range(len(List_)):
        if 1<=List_[j][0]<=ch and 1<=List_[j][1]<=ch:
            if data_1.index(List_[j][0])>data_1.index(List_[j][1]):
                count+=1
    if count==n:
        print "YES"
    else:
        print "NO"
    
a,b,c,d = map(int,raw_input().split())
subNum = map(str,raw_input().split())
l2 =[]
 
for i in range(a,b+1):
    for j in range(d):
        if subNum[j] in str(i):
            l2.append(i)  
        
if len(l2)>0:
    l2.sort()
    print l2[c-1]
else:
    print "DOES NOT EXIST"
            

