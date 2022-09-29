from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
ax = deque([(0,0)])
visited = [[False]*n for _ in range(n)]

def DFS(board,x,y,color):
    if board[x][y] != color:
        return
    visited[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            DFS(nx,ny,color)

cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            DFS(i,j,board[i][j])

print(cnt)