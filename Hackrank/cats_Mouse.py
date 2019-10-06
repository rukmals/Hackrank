q=input()
if 1<=q<=100:
    def F_Pos(List):
        A=List[0]
        B=List[1]
        C=List[2]
        x=abs(C-B)
        y=abs(C-A)
        if 1<=A<=100 and 1<=B<=100 and 1<=C<=100:
        if x>y:
            return "Cat A"
        if x<y:
            return "Cat B"
        else:
            return "Mouce C"    
    for i in range(q):
        List = list(map(int,raw_input().strip().split(' ')))
        print F_Pos(List)
        
