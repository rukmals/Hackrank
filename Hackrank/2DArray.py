import sys
#1 1 1 0 0 0
#0 1 0 0 0 0
#1 1 1 0 0 0
#0 0 2 4 4 0
#0 0 0 2 0 0
#0 0 1 2 4 0
#List = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
List = []
for k in range(0,6):
    data = list(map(int,sys.stdin.readline().split()))
    List.append(data)

def Function(List):
    Sum = []
    for i in range(0,4):
        if -9<=List[i]<=9:
            x = List[i:i+3]
            Sum.append(sum(x))
    return Sum
def Function_1(L):
    Var = []
    for j in range(1,5):
        if -9<=L[j]<=9:
            Var.append(L[j])
    return Var

Sum_List = []
for i in range(0,4):
    x,y,z = Function(List[i]), Function_1(List[i+1]) , Function(List[i+2])
    for j in range(len(x)):
        Sum_List.append(x[j]+y[j]+z[j])
print max(Sum_List)
    
