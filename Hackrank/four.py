List = raw_input().strip().split(":")
Var = List[2][2:4]
Hour = int(List[0])
Min = int(List[1])
Sec = int(List[2][0:2])
if 0<=Hour<=12 and 0<=Min<=59 and 0<=Sec<=59:
    if Var == 'PM' and Hour!=12:
        print str(12+Hour)+":"+List[1]+":"+List[2][0:2]
    if Var == "AM" and Hour!=12:
        print List[0]+":"+List[1]+":"+List[2][0:2]
    if Hour == 12 and Var == "PM":
        print str(Hour)+":"+List[1]+":"+List[2][0:2]
    if Hour == 12 and Var == "AM":
        print "00"+":"+List[1]+":"+List[2][0:2]
    
    

    

        
        

        

