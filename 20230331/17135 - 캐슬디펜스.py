import sys
sys.stdin = open('input.txt','rt')

N,M,D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]

from collections import deque

def attack(x,y):
    '''
    x,y 는 궁수위치 -> 어디칸이 먼저 닿는지?
    '''
    deq = deque([(x-1,y,1)])
    visited = [[False]*M for _ in range(N)]
    visited[x-1][y] = True
    distance = N+M+2
    ax = []

    while deq:
        x,y,dist = deq.popleft()

        if dist > distance:
            break

        if arr[x][y] == 1:
            distance = dist
            if dist <= D:
                ax.append((x,y))
            else:
                break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M or visited[nx][ny]:
                continue
        
            visited[nx][ny] = True
            deq.append((nx,ny,dist+1))
    
    if len(ax) == 0:
        return -1,-1
    x,y = sorted(ax, key= lambda x: x[1])[0]
    return x,y

def attack_all(pos):
    ax,die = [],0 #도둑 좌표
    
    for x,y in pos:
        ax.append(attack(x,y))

    for x,y in ax:
        if x == -1 and y == -1:
            continue
        if arr[x][y] == 0:
            continue
        die += 1
        arr[x][y] = 0

    return die
    
def move():
    global arr

    flag = False
    arr_ = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if i+1 >= N: 
                    continue
                else:
                    arr_[i+1][j] = 1
                    flag = True #한명이라도 살아 남은 경우 게임은 다시 진행한다
    arr = arr_
    return flag

all_position = []
def DFS(depth,s,res):
    if depth == 3:
        all_position.append(res)
        return
    for i in range(s,M):
        DFS(depth+1,i+1,res+[(N,i)])

DFS(0,0,[])
answer = 0

def debug():
    for a in arr:
        print(a)
    print()

for pos in all_position:
    tmp = [a[:] for a in arr]
    die = 0
    flag = True
    while flag:
        die += attack_all(pos)
        flag = move()
    answer = max(answer,die)
    arr = tmp

print(answer)

