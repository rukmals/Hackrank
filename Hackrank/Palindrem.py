def P(word):
    if word[0]==word[len(word)-1]:
        return True
def P_1(word):
    if word==word[::-1]:
        return True
word = "raceofcars"
word_List=list(word)
word_List_2,word_List_3=[],[]
List,List_,List_1=[],[],[]
for i in range(len(word)):
    for j in range(i+1,len(word)+1):
        word_List_2.append("".join(word_List[i:j]))
        if P("".join(word_List[i:j]))==True and len(word_List[i:j])>1:
            List.append("".join(word_List[i:j]))
for x in List:
    if P_1(x)==True:
        List_1.append(len(x))
    
print List_1

