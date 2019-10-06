n=input()
if 1<=n<=100:
    arr  = list(map(int,raw_input().strip().split(' ')))
    arr_ = list(set(arr))
    count = 0
    for element in arr_:
        if 1<=element<=100:
            count+=arr.count(element)//2  
    print count
