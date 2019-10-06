Length =list(map(int,raw_input().strip().split(' ')))
first = list(map(int,raw_input().strip().split(' ')))
second = list(map(int,raw_input().strip().split(' ')))
List_1=[]
if 1<=Length[0]<=10 and 1<Length[1]<=10 and 1<=max(first)<=100 and 1<=max(second)<=100:
    for i in range(1,min(second)+1):
        List=[]
        for j in range(len(first)):
            List.append(i%first[j])
        if sum(List)==0:
            List_1.append(i)
    List_3=[]
    for k in List_1:
        List_2=[]
        for x in range(len(second)):
            List_2.append(second[x]%k)
        if sum(List_2)==0:
            List_3.append(k)
    print len(List_3)
