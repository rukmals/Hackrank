import sys
number = input()
if 0<number<=100:
    data = list(map(int,sys.stdin.readline().split()))
    positive = len(list(data[i] for i in range(len(data)) if data[i]>0 and -100<=data[i]<=100))
    print str.format('{0:.6f}',positive/float(len(data)))
    negative = len(list(data[j] for j in range(len(data)) if data[j]<0 and -100<=data[j]<=100))
    print str.format('{0:.6f}',negative/float(len(data)))           
    zero = len(list(data[k] for k in range(len(data)) if data[k]==0 and -100<=data[k]<=100))
    print str.format('{0:.6f}',zero/float(len(data)))

