from collections import deque

n,m,t = map(int,input().split())
game = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
answer = -1

dist = [[-1]*m for _ in range(n)]
dist[0][0] = 0
deq = deque([(0,0)])
midDist = -1

while deq:
    x,y = deq.popleft()
    if game[x][y] == 2: 
        midpoint = (x,y)
        midDist = dist[x][y]
    if x == (n-1) and y == (m-1):
        deq = deque([])
        answer = dist[x][y]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m: 
            if game[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                deq.append((nx,ny))

if midDist != -1:
    dist = [[-1]*m for _ in range(n)]
    x,y = midpoint
    dist[x][y] = 0 
    deq = deque([(x,y)])

    while deq:
        x,y = deq.popleft()
        if x == (n-1) and y == (m-1):
            if answer == -1:
                answer = dist[n-1][m-1] + midDist
            else:
                answer = min(dist[n-1][m-1] + midDist,answer)
            deq = deque([])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m: 
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    deq.append((nx,ny))

if 0<=answer<= t:
    print(answer)
else:
    print("Fail")

'''
7 7 100
0 0 0 0 0 0 0
0 1 1 1 1 1 2
0 0 0 0 0 0 0
1 1 1 0 1 1 1
0 0 0 0 0 0 1
0 1 1 1 1 1 1
0 0 0 0 0 0 0

5 4 100
0 1 2 1
0 1 0 1
0 0 0 0
1 1 1 1
0 0 0 0
'''

