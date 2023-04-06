N, M = 12, 6

from collections import deque
dx, dy = [1,0,-1,0],[0,1,0,-1]
arr = [list(input()) for _ in range(N)]

def find_group(x,y,color):
    
    deq = deque([(x,y)])
    visited[x][y] = True
    ax = [(x,y)]

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                ax.append((nx,ny))
                deq.append((nx,ny))

    return ax

def explode():
    global flag

    for x in range(N):
        for y in range(M):
            if arr[x][y] != '.' and not visited[x][y]:
                ax = find_group(x,y,arr[x][y])
                if len(ax) <= 3:
                    continue
                flag = True
                for x,y in ax:
                    arr[x][y] = '.'

def down():
    for y in range(M):
        index = N-1
        for x in range(N-1,-1,-1):
            if arr[x][y] != '.':
                arr[index][y] = arr[x][y]
                index -= 1
        for x in range(index,-1,-1):
            arr[x][y] = '.'

answer = 0
flag = True

while flag:
    flag = False
    visited = [[False]*M for _ in range(N)]
    explode()
    if flag: answer += 1
    down()

print(answer)