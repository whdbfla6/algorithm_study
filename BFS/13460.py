from collections import deque

n,m = map(int,input().split())
game = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if game[i][j] == 'R': red = (i,j)
        if game[i][j] == 'B': blue = (i,j)
        if game[i][j] == '#': visited[i][j] = True

dx = [0,1,-1,0]
dy = [1,0,0,-1]

axis = deque([(red,blue,1)])

while axis:
    r,b,cnt = axis.popleft()
    if cnt >= 10:
        print(-1)
        exit()
    for i in range(4):
        rgoal = False
        rx,ry = r
        bx,by = b
        visited[rx][ry] == True
        while True:
            rx += dx[i]
            ry += dy[i]
            if visited[rx][ry] == False:
                if game[rx][ry]=='B':
                    rx -= dx[i]
                    ry -= dy[i]
                    break
                visited[rx][ry] = True
                if game[rx][ry] == 'O':
                    rgoal = True
            else:
                rx -= dx[i]
                ry -= dy[i]
                break
        while True:
            bx += dx[i]
            by += dy[i]
            if game[bx][by] == 'O':
                break
            if game[bx][by] == '#' or (bx==rx and by==ry):
                bx -= dx[i]
                by -= dy[i]
                if rgoal:
                    print(cnt)
                    exit()
                axis.append(((rx,ry),(bx,by),cnt+1))
                break

print(-1)