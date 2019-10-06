b_=list(map(int,raw_input().strip().split(' ')))
b=b_[0]
n=b_[1]
m=b_[2]
if 1<=n<=1000 and 1<=m<=1000 and 1<=b<=10**6:
    keyboard=list(map(int,raw_input().strip().split(' ')))
    usb=list(map(int,raw_input().strip().split(' ')))
    amount = []
    for x in keyboard:
        for y in usb:
            if x+y<=b:
                amount.append(x+y)
    if len(amount)>0:
        print max(amount)
    else:
        print -1
                
