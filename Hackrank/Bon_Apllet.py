List=list(map(raw_input().strip().split(' ')))
n=List[0]
if 2<=n<=10**5:
    bill=list(map(raw_input().strip().split(' ')))
    b=input()
    if 0<=List[1]<n:
        Alagic = bill.pop(List[1])
        #print Alagic
        if sum(bill)//2==b:
            print "Bon Appetit"
        else:
            print b-sum(bill)//2
            

