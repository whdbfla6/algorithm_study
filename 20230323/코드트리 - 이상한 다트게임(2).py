import sys
sys.stdin = open('20230323/input.txt','rt')

from collections import deque
import copy

N,M,Q = map(int,input().split())
wonpan = [[]]

for i in range(N):
    wonpan.append(deque(map(int,input().split())))

rotateinfo = [tuple(map(int,input().split())) for _ in range(Q)]

def rotate(x,d,k): #회전
    if d == 0:
        for i in range(x,N+1,x):
            for _ in range(k): wonpan[i].appendleft(wonpan[i].pop()) #시계방향
    else:
        for i in range(x,N+1,x):
            for _ in range(k): wonpan[i].append(wonpan[i].popleft())

def same_value_check():
    global flag
    
    for i in range(1,N):
        for j in range(M):
            if wonpan[i][j] == 0:
                continue
            if wonpan[i][j] == wonpan[i][j-1]:
                flag = False
                wonpan_[i][j] = wonpan_[i][j-1] = 0
            if wonpan[i][j] == wonpan[i+1][j]:
                flag = False
                wonpan_[i][j] = wonpan_[i+1][j] = 0

    for j in range(M):
        if wonpan[N][j] == 0:
            continue
        if wonpan[N][j] == wonpan[N][j-1]:
            flag = False
            wonpan_[N][j] = wonpan_[N][j-1] = 0

def wonpan_avg(): #평균 구하기위해 summ,cnt 구하기
    summ,cnt = 0,0
    for i in range(1,N+1):
        for j in range(M):
            if wonpan[i][j]>0:
                summ += wonpan[i][j]
                cnt += 1
    return summ,cnt

def normalization(avg): #정규화 작업
    for i in range(1,N+1):
        for j in range(M):
            if wonpan[i][j]==0:
                continue
            if wonpan[i][j] > avg:
                wonpan[i][j] -= 1
            elif wonpan[i][j] < avg:
                wonpan[i][j] += 1


for x,d,k in rotateinfo:
    rotate(x,d,k)
    flag = True
    wonpan_ = copy.deepcopy(wonpan)
    same_value_check()
    wonpan = wonpan_

    if flag:
        summ,cnt = wonpan_avg()
        if cnt > 0:
            avg = summ//cnt
            normalization(avg)

answer,_ = wonpan_avg()
print(answer)

