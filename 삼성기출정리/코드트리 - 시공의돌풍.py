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

def anticlock():
    dx, dy = [0,-1,0,1],[1,0,-1,0]
    x,y,d = ux,0,0
    prev = arr[x][y]

    while True:
        nx, ny = x+dx[d], y+dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            d = (d+1)%4
            nx, ny = x+dx[d], y+dy[d]
        arr[nx][ny], prev = prev, arr[nx][ny]
        x, y = nx, ny
        if x == ux and y == 0:
            break
    arr[ux][1] = 0

def clock():
    dx, dy = [0,1,0,-1],[1,0,-1,0]
    x,y,d = lx,0,0
    prev = arr[x][y]

    while True:
        nx, ny = x+dx[d], y+dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=M:
            d = (d+1)%4
            nx, ny = x+dx[d], y+dy[d]
        arr[nx][ny], prev = prev, arr[nx][ny]
        x, y = nx, ny
        if x == lx and y == 0:
            break
    arr[lx][1] = 0



def clean():
    global arr
    anticlock()
    clock()
    arr[lx][0] = arr[ux][0] = -1

for _ in range(T):
    expand()
    clean()

answer = 0
for i in range(N):
    for j in range(M):
        answer += arr[i][j]
answer += 2
print(answer)