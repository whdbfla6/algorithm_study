from collections import deque

n,m = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(n)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def inside_area():
    visited = [[False]*m for _ in range(n)]
    deq = deque([(0,0)])
    cheeze[0][0] = -1

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0<=newx<n and 0<=newy<m and visited[newx][newy] == False and cheeze[newx][newy] != 1:
                visited[newx][newy] = True
                cheeze[newx][newy] = -1 
                deq.append((newx,newy))

def melting():
    axis= []
    for i in range(1,n-1):
        for j in range(1,m-1):
            if cheeze[i][j] == 1:
                cnt = 0
                for k in range(4):
                    newx = i + dx[k]
                    newy = j + dy[k]
                    if cheeze[newx][newy] == -1: cnt +=1
                    if cnt == 2: 
                        axis.append((i,j))
                        break

    return axis

time = 0

while True:
    inside_area()
    axis = melting()
    if len(axis) == 0:
        break
    for a in axis:
        cheeze[a[0]][a[1]] = 0
    time += 1

print(time)




