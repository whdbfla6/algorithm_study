from collections import deque

n,k = map(int,input().split())
virusmap = [list(map(int,input().split())) for _ in range(n)]
S,X,Y = map(int,input().split())

axis = deque([])

for v in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if virusmap[i][j] == v: axis.append((i,j,v,0))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while axis:
    x,y,virus,s = axis.popleft()
    if s == S:
        break
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0<=newx<=n-1 and 0<=newy<=n-1 and virusmap[newx][newy] == 0:
            virusmap[newx][newy] = virus
            axis.append((newx,newy,virus,s+1))

print(virusmap[X-1][Y-1])
