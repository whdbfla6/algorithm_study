import sys
sys.stdin = open('input.txt','rt')

from collections import deque
N,M,Q = map(int,input().split())
wonpan = [deque(map(int,input().split())) for _ in range(N)] # 0 시계 1 반시계
info = [tuple(map(int,input().split())) for _ in range(Q)]

def rotate(x,d,k):
    if d == 1: k = -k
    for i in range(x,N+1,x):
        wonpan[i-1].rotate(k)

def remove_number():
    global wonpan, FLAG
    wonpan_ = [list(w)[:] for w in wonpan]
    
    for i in range(N):
        for j in range(M):
            prev, cur = wonpan[i][j-1], wonpan[i][j]
            if cur == 0: continue
            if prev == cur: 
                FLAG = True
                wonpan_[i][j-1] = wonpan_[i][j] = 0

    for j in range(M):
        for i in range(N-1):
            cur, next = wonpan[i][j], wonpan[i+1][j]
            if cur == 0: continue
            if cur == next:
                FLAG = True
                wonpan_[i][j] = wonpan_[i+1][j] = 0

    wonpan = wonpan_

def normalize():
    summ, cnt = 0,0

    for i in range(N):
        for j in range(M):
            if wonpan[i][j] == 0:
                continue
            summ += wonpan[i][j]
            cnt += 1

    if cnt == 0: return
    avg = summ // cnt

    for i in range(N):
        for j in range(M):
            if wonpan[i][j] == 0:
                continue
            if wonpan[i][j] > avg:
                wonpan[i][j] -= 1
            if wonpan[i][j] < avg:
                wonpan[i][j] += 1

for x,d,k in info:
    rotate(x,d,k)
    FLAG = False #지워진 수가 없다
    remove_number()
    if not FLAG:
        normalize()
    wonpan = list(map(deque,wonpan))

answer = sum(map(sum,wonpan))
print(answer)