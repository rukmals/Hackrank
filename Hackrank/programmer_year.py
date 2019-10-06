while 1:
    def Leap(year):
        if year%4==0:
            if year%100==0:
                if year%400 ==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    def Leap_(year):
        if year%4==0:
            return True
        else:
            return False
            
    #print Leap_(1800)
    #print Leap(2016)
    #Leap = [31,29,31,30,31,30,31,31]
    #Not_Leap = [31,28,31,30,31,30,31,31]
    #year_1918 = [31,15,31,30,31,30,31,31,30]
    year = input()
    if 1700<=year<=1917:
        if Leap_(year)==True:
            print "12.09."+`year`
        else:
            print "13.09."+`year`
    elif year == 1918:
        print "26.09.1918"
    elif 1918<year<=2700:
        if Leap(year)==True:
            print "12.09."+`year`
        else:
            print "13.09."+`year`
        
