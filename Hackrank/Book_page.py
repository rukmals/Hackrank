n=input()
if 1<=n<=1000:
    score = list(map(int,raw_input().strip().split(' ')))
    est_point_H = score[0]
    est_point_L = score[0]
    count,count_=0,0
    for i in range(1,len(score)):
        if 0<=score[i]<=10**8:
            if score[i]>est_point_H:
                est_point_H = score[i]
                #print est_point_H
                count+=1
            if score[i]<est_point_L:
                est_point_L = score[i]
                #print est_point_L
                count_+=1
    print count,count_
