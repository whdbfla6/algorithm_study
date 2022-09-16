from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
check = [[True]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0: check[i][j] = False

dx = [1,0,-1,0]
dy = [0,1,0,-1]

axis = deque([(0,0)])
check[0][0] = False

while axis:
    x,y = axis.popleft()
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0<=newx<=n-1 and 0<=newy<=m-1 and check[newx][newy]:
            board[newx][newy] += board[x][y]
            check[newx][newy] = False
            axis.append((newx,newy))

print(board[n-1][m-1])


