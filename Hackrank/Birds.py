#from collections import OrderedDict
#print list(OrderedDict.fromkeys(arr))
#print list(dict.fromkeys("aasssddeecc"))
n=input()
arr = list(map(int,raw_input().strip().split(' ')))
element_List = list(set(arr))
count_List = []
for element in element_List:
    count_List.append(arr.count(element))
#print count_List
print element_List[count_List.index(max(count_List))]
#print count_List.count(max(count_List))


