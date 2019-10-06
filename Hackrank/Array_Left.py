#d=4
#List = [1,2,3,4,5]
Num_List = map(int,raw_input().strip().split(' '))
n=Num_List[0]
d=Num_List[1]
List = map(int,raw_input().strip().split(' '))
if 1<=n<=10**5:
    if 1<=d<=n:
        for i in range(d):
            if 1<=List[i]<=10**6:
                a=List.pop(0)
                List_1 = List
                List_1.append(a)
        for j in range(len(List_1)):
            print List_1[j],
           
