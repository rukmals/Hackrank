n=input()
LB = list(map(int,raw_input().strip().split(' '))) #[100,100,50,40,40,20,10]
LB_=list(set(LB))
m=input()
AM=list(map(int,raw_input().strip().split(' '))) #[5,25,50,120]
#rank=[]
if 1<=n<=2*10**5 and 1<=m<=2*10**5:
    List_ = list(set(LB))
    List_.sort()
    List = List_[::-1]
    print List #[100,50,40,20,10]
    for mark in range(len(AM)):
        if 0<=AM[mark]<=10**9:
            if AM[mark]>=max(List):
                #rank.append(1)
                print 1
            elif AM[mark]<min(List):
                #rank.append(len(List)+1)
                print len(List)+1
            elif AM[mark] in List:
                #rank.append(List.index(AM[mark])+1)
                print List.index(AM[mark])+1
            else:
                for i in range(len(List)):
                    if 0<=List[i]<=10**9:
                        if List[i]>AM[mark]>List[i+1]:
                            #rank.append(i+2)
                            print i+2
            #print rank            
