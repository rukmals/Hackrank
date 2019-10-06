n=input()
if 2<=n<=10**6:
    step= list(raw_input().strip()) #["U","D","D","D","U","D","U","U"]
    #print step
    count = 0
    count_List=[]
    for i in range(len(step)):
        if step[i]=="U":
            count+=1
        else:
            count-=1
        count_List.append(count)
    val=0
    for j in range(len(count_List)):
        if count_List[j]==0 and count_List[j-1]==-1:
            val+=1
    print val
            
