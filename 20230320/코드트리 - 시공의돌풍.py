from collections import deque
import copy

N,M,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
wind = []

for i in range(N):
    if arr[i][0] == -1: wind.append(i)
ux,lx = wind

def expand():
    global arr
    arr_ = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                dust = arr[i][j]
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=M or arr[nx][ny]==-1:
                        continue
                    arr_[nx][ny] += dust//5
                    arr_[i][j] -= dust//5
    arr = arr_

def clean():
    global arr
    arr_ = copy.deepcopy(arr)
    arr_[ux][1] = 0
    arr_[lx][1] = 0

    for i in range(1,M-1): 
        arr_[ux][i+1] = arr[ux][i]
        arr_[lx][i+1] = arr[lx][i]

    for i in range(ux,0,-1):
        arr_[i-1][-1] = arr[i][-1]
    for i in range(lx,N-1):
        arr_[i+1][-1] = arr[i][-1]

    for i in range(M-1,0,-1):
        arr_[0][i-1] = arr[0][i]
        arr_[-1][i-1] = arr[-1][i]

    for i in range(0,ux-1):
        arr_[i+1][0] = arr[i][0]
    for i in range(lx+2,N):
        arr_[i-1][0] = arr[i][0]
    arr = arr_

for _ in range(T):
    expand()
    clean()

answer = 0
for i in range(N):
    for j in range(M):
        answer += arr[i][j]
answer += 2 #돌풍
print(answer)