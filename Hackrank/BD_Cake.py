while 1:
    n=input()
    squre=list(map(int,raw_input().strip().split(' ')))
    day_month = list(map(int,raw_input().strip().split(' ')))
    day = day_month[0]
    month = day_month[1]
    if 1<=day<=31 and 1<=month<=12:
        count = 0
        for i in range(len(squre)-month+1):
            if 1<=squre[i]<=5 and 0<=i<n:
                if sum(squre[i:i+month])==day:
                    count+=1
        print count
