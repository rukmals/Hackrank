t=input()
for i in range(t):
    data = list(map(int,raw_input().strip().split(' ')))
    data_ = list(map(int,raw_input().strip().split(' ')))
    n=data[0]
    k=data[1]
    count=0
    for j in range(len(data_)):
        if data_[j]<=0:
            count+=1
    if k>count:
        print "YES"
    else:
        print "NO"
   
