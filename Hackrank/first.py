'''import sys
number = input()
List = []
for i in range(0,number):
    data = list(map(int,sys.stdin.readline().split()))
    List.append(data[0:number])
sum_1 = sum(List[j][j] for j in range(number) if -100<=List[j][j]<=100)
sum_2 = sum(List[k][number-k-1] for k in range(number) if -100<=List[k][number-k-1]<=100)
print (sum_1-sum_2)
n=input()
for i in range(1,n+1):
    print " "*(n-i)+"#"*i'''

'''import sys
import itertools
print list(itertools.takewhile(lambda x: x.strip() != 'quit', sys.stdin))
print list(iter(raw_input,'quit'))  
from sys import stdin
lines = stdin.read().splitlines()
print lines'''
import sys
print(len(sys.stdin.read()))
