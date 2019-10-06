n=input()
Grd = []
for i in range(n):
    mark = input()
    Grd.append(mark)
Mod_Grd=[]
for grd in Grd:
    if 0<=grd<=100:
        if grd>=38:
            reminder=5-grd%5
            if reminder<3:
                Mod_Grd.append(grd+reminder)
            else:
                Mod_Grd.append(grd)
        else:
            Mod_Grd.append(grd)
print Mod_Grd
    
