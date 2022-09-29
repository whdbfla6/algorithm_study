import sys
sys.setrecursionlimit(10**6)

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

def func(w,h):
    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    def DFS(x,y):
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and board[nx][ny]==1:
                visited[nx][ny] = True
                DFS(nx,ny)

    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j]==1:
                visited[i][j] = True
                DFS(i,j)
                cnt += 1
    print(cnt)

while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    else:
        func(w,h)
