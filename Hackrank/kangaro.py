L = list(map(int,raw_input().strip().split(' ')))
x1=L[0]
v1=L[1]
x2=L[2]
v2=L[3]
for i in range(1000):
    x1,x2=x1+v1,x2+v2
    if x1==x2:
        print "Yes"
        break
else:
    print "No"
