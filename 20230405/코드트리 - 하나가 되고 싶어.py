import sys
sys.stdin = open('input.txt','rt')

N = int(input())
arr = [list(input()) for _ in range(N)]

answer = N**2
dx,dy = [1,0,-1,0], [0,1,0,-1]

blanknum = 0
sx,sy = None, None

for x in range(N):
    for y in range(N):
        if arr[x][y] == '.': 
            sx,sy = x,y
            blanknum += 1

from collections import deque
visited = [[False]*N for _ in range(N)]

def BFS(x,y):

    deq = deque([(x,y)])

    visited2 = [[False]*N for _ in range(N)]
    
    visited2[x][y] = True
    visited[x][y] = True
    cnt = 1

    ax = []
            
    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited2[nx][ny]:
                continue
            
            visited2[nx][ny] = True
            
            if arr[nx][ny] == '#':
                ax.append((nx,ny))

            if not visited[nx][ny] and arr[nx][ny] == '.':
                visited[nx][ny] = True
                deq.append((nx,ny))
                cnt += 1

    return ax, cnt

def DFS(x,y,summ,cnt,total): #들른 빈칸 개수, 부순 벽돌 개수, 전체 빈칸 개수
    global answer,visited

    if cnt > answer:
        return
    
    visited_ = [v[:] for v in visited]
    ax, summ_ = BFS(x,y)

    if summ + summ_ == total:
        answer = min(answer,cnt)
        return

    for nx, ny in ax:
        arr[nx][ny] = '.'
        DFS(nx,ny,summ+summ_,cnt+1,total+1)
        arr[nx][ny] = '#'
    visited = visited_

DFS(sx,sy,0,0,blanknum)

if answer > 6:
    print(-1)
else:
    print(answer)