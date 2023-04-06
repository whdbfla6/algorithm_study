# 0빈칸 1/ 2\ 3모름
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ax = [] #3인 좌표들

for i in range(N):
    for j in range(N):
        if arr[i][j] == 3: ax.append((i,j))

def DFS(depth,res):
    if depth == len(ax):
        prob.append(res)
        return
    
    for i in range(3):
        DFS(depth+1,res+[i])

from collections import deque

tmp = deque(map(int,input().split()))
dx,dy = [1,0,-1,0],[0,1,0,-1] # 아래,오,위,왼 -> 시계방향

BALLN = sum(tmp)
def ball_position():
    global BALLN
    for i in range(N):
        x = tmp.popleft()
        if x: ball[0][i].append(0)
    for i in range(N):
        x = tmp.popleft()
        if x: ball[i][N-1].append(3)
    for i in range(N-1,-1,-1):
        x = tmp.popleft()
        if x: ball[N-1][i].append(2)
    for i in range(N-1,-1,-1):
        x = tmp.popleft()
        if x: ball[i][0].append(1)

def change_direction(s,d):  # 아래,오,위,왼
    if s == 1:
        if d == 0: return 3
        if d == 2: return 1
        if d == 1: return 2
        if d == 3: return 0
    if s == 2:
        if d == 0 or d == 2: return d+1
        if d == 1 or d == 3: return d-1
    return d

def crash_all():
    for x in range(N):
        for y in range(N):
            if len(ball[x][y]) >= 2:
                ball[x][y] = []

def move():
    global CNT, ball
    ball_ = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            for d in ball[x][y]:
                d = change_direction(arr[x][y],d)
                nx, ny = x+dx[d], y+dy[d]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    CNT+=1
                    continue
                ball_[nx][ny].append(d)
    ball = ball_

def check():
    for x in range(N):
        for y in range(N):
            if len(ball[x][y]) > 0: return True
    return False

prob = []
DFS(0,[])
ball = [[[] for _ in range(N)] for _ in range(N)]
ball_position()

answer= 0
CNT = 0 # 밖으로 나간 구슬, 충돌한 구슬

def simulation(p):
    global ball, arr, CNT, answer

    ball_ = [[b[:] for b in row] for row in ball]
    arr_ = [a[:] for a in arr]
    for s,(x,y) in zip(p,ax):
        arr[x][y] = s
    
    status = True
    while status:
        crash_all()
        move()
        status = check()

    answer = max(answer,CNT)
    ball = ball_
    arr = arr_
    CNT = 0

for p in prob:
    simulation(p)

print(answer)