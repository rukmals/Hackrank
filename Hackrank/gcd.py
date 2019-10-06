#from fractions import gcd
#print gcd(20,8)
import sys
n=input()
l=list(map(int,raw_input().strip().split(' ')))
m=input()
for j_ in range(m):
    List_2=[]
    magic=map(int,sys.stdin.readline())
    for i_ in l:
        if i_==magic:
            List_2.append(1)
    #l=[2,3,5,6,6]
    List=[]
    for i in range((len(l)//2)+1):
        x=l[i]
        y=l
        z=y.pop(i)
        L=y
        for j in range(len(L)):
            for k in range(j,len(L)):
                List.append(L[j:k+1]+[z])
        y.insert(i,x)
        #print i,x,z,y
    print List
    def find_gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    for x in List:
        l_=x
        n1=l_[0]
        n2=l_[1]
        gcd = find_gcd(n1,n2)
        for i in range(2,len(l_)):
            gcd = find_gcd(gcd,l_[i])
        if gcd==magic:
            List_2.append(1)
    print len(List_2)
