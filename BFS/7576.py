from collections import deque
m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

deq = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1: deq.append((i,j))

dx,dy = [0,1,0,-1],[1,0,-1,0]

while deq:
    x,y = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            deq.append((nx,ny))

answer = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        if tomato[i][j]>0:
            answer = max(answer,tomato[i][j])

print(answer-1)