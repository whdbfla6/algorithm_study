from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]

walls = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == 1: walls.append((i,j))

# 부수기 전, 부순 후 두 경우에 대해 리스트 생성 
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
ax = deque([(0,0,0)])
dx,dy = [0,1,0,-1],[1,0,-1,0]

while ax:
    x,y,w = ax.popleft()
    if x == n-1 and y == m-1:
        print(visited[x][y][w])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            # 통과 가능하고 방문 안 한 경우(w=0 or w=1)
            if board[nx][ny] == 0 and visited[nx][ny][w] == -1:
                visited[nx][ny][w] = visited[x][y][w] + 1
                ax.append((nx,ny,w))
            # 벽이지만 부수지 않은 경우
            if board[nx][ny] == 1 and w==0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                ax.append((nx,ny,1))
print(-1)
