import sys
Str = []
Qur = []
n=input()
for j in range(n):
    data = sys.stdin.readline()
    Str.append(data)
m=input()
for k in range(m):
    data_1 = sys.stdin.readline()
    Qur.append(data_1)
if 1<=n<=1000 and 1<=m<=100 and 1<=len(Str)<=20 and 1<=len(Qur)<=20:
    for i in range(len(Qur)):
        print Str.count(Qur[i])
    
