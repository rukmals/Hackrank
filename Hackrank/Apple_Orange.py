s_t=list(map(int,raw_input().strip().split(" ")))
s=s_t[0]
t=s_t[1]
a_b=list(map(int,raw_input().strip().split(" ")))
a=a_b[0]
b=a_b[1]
c_a_b=list(map(int,raw_input().strip().split(" ")))
c_a=3
c_b=3
Apple = list(map(int,raw_input().strip().split(" ")))
Orange = list(map(int,raw_input().strip().split(" ")))
if 1<=s<=10**5 and 1<=t<=10**5 and 1<=a<=10**5 and 1<=b<=10**5 and 1<=c_a<=10**5 and 1<=c_b<=10**5 and a<s<t<b:
    count_Apple,count_Orange = 0,0
    for place_Apple in Apple:
        if -10**5<=place_Apple<=10**5:
            Var_1 = place_Apple+a
            if s<=Var_1<=t:
                count_Apple+=1
    for place_Orange in Orange:
        if -10**5<=place_Orange<=10**5:
            Var_2 = place_Orange+b
            if s<=Var_2<=t:
                count_Orange+=1
    print count_Apple
    print count_Orange
            
        
        
