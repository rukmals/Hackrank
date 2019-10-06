import sys
n = input()
if 1<=n<=10**5:
    data = list(map(int,sys.stdin.readline().split()))
    item_1 = max(data)
    data.remove(item_1)
    Max_List = []
    for item in data:
        if 1<=item<=10**7:
            if item==item_1:
                Max_List.append(item)

    print len(Max_List)+1
