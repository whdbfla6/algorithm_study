import sys
sys.stdin = open('input.txt','rt')

n,Q = map(int,input().split())
N = 2**n
ice = [list(map(int,input().split())) for _ in range(N)]
levels = list(map(int,input().split()))

dx,dy = [0,1,0,-1],[1,0,-1,0]

def rotate_all(level):
    global ice
    size = 2**level
    inside_size = 2**(level-1)

    ax = [(0,0),(0,inside_size),(inside_size,inside_size),(inside_size,0)]
    ice_ = [[0]*N for _ in range(N)]

    for x in range(0,N,size):
        for y in range(0,N,size):
            d = 0
            for i,j in ax:
                for x_ in range(x+i,x+i+inside_size):
                    for y_ in range(y+j,y+j+inside_size):
                        ice_[x_+dx[d]*inside_size][y_+dy[d]*inside_size] = ice[x_][y_]
                d = (d+1)%4
                
    ice = ice_

import copy

def melt():
    global ice
    ice_ = copy.deepcopy(ice)
    for x in range(N):
        for y in range(N):
            if ice[x][y] == 0:
                continue
            cnt = 0 
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<N and 0<=ny<N and ice[nx][ny]>0:
                    cnt += 1
            if cnt < 3: ice_[x][y] -= 1
    ice = ice_

from collections import deque
def get_group_size(x,y):

    deq = deque([(x,y)])
    cnt = 0
    
    while deq:
        x,y = deq.popleft()
        cnt += 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and ice[nx][ny] > 0:
                visited[nx][ny] = True
                deq.append((nx,ny))  

    return cnt     

for level in levels:
    if level > 0 :
        rotate_all(level)
    melt()

# for a in ice:
#     print(a)
# print()

amount, size = 0,0
visited = [[False]*N for _ in range(N)]

for x in range(N):
    for y in range(N):
        amount += ice[x][y]
        if ice[x][y] > 0 and not visited[x][y]:
            visited[x][y] = True
            size = max(size,get_group_size(x,y))

print(amount)
print(size)

