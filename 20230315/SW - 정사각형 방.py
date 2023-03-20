T = int(input())
dx,dy = [1,0,-1,0],[0,1,0,-1]

def DFS(x,y,cnt):
    global maxcnt, roomnum

    move = 4
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny] or arr[nx][ny] != arr[x][y]+1:
            move -= 1
            continue

        visited[nx][ny] = True
        DFS(nx,ny,cnt+1)
        visited[nx][ny] = False

    if not move:
        if cnt > maxcnt:
            maxcnt = cnt
            roomnum = num
        elif cnt == maxcnt:
            roomnum = min(roomnum,num)


for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    maxcnt,roomnum = 0,0

    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            num = arr[i][j]
            DFS(i,j,1)
            visited[i][j] = False

    print('#{} {} {}'.format(t,roomnum,maxcnt))
