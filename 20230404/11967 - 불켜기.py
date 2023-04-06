import sys
sys.stdin = open('input.txt','rt')

from collections import deque, defaultdict
N,M = map(int,input().split())
dic = defaultdict(lambda:[])

for _ in range(M):
    x,y,a,b = map(int,input().split())
    dic[(x-1,y-1)].append((a-1,b-1))

light = [[False]*N for _ in range(N)] #불이 켜졌는가?
light[0][0] = True

visited = [[False]*N for _ in range(N)] #방문한 적이 있는가?
visited[0][0] = True

deq = deque([(0,0)])
dx,dy = [1,0,-1,0],[0,1,0,-1]
CNT = 1

while deq:
    x,y = deq.popleft()

    next = []
    for a,b in dic[(x,y)]:
        if not light[a][b]:
            light[a][b] = True
            CNT += 1
            for i in range(4):
                na, nb = a+dx[i], b+dy[i]
                if 0<=na<N and 0<=nb<N and visited[na][nb]:
                    visited[a][b] = True
                    deq.append((a,b))
                    break

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and light[nx][ny]:
            visited[nx][ny] = True
            deq.append((nx,ny))

print(CNT)