
Input = map(int,raw_input().strip().split(' '))
n=Input[0]
m=Input[1]
List = []
for k in range(m):
     data = map(int,raw_input().strip().split(' '))
     List.append(data)
     

if 3<=n<=10**7 and 1<=m<=2*10**5:
    start = []
    end = []
    value =[]
    Zero = [0]*n
    '''for i in range(len(List)):
        start.append(List[i][0]-1)
        end.append(List[i][1])
        value.append(List[i][2])'''
    for j in range(0,m):
        if 1<=List[j][0]<=List[j][1]<=n:#and 0<=value[j]<10**9:
            start.append(List[j][0]-1)
            end.append(List[j][1])
            value.append(List[j][2])
            if 0<=value[j]<10**9:
                List_1= [x+value[j] for x in Zero[start[j]:end[j]]]
                Zero[start[j]:end[j]] = List_1
            #print Zero
    print max(Zero)

