import sys
sys.stdin = open('input.txt','rt')

from collections import defaultdict

nums = [str(i) for i in range(1,10)]
N = int(input())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S': sx,sy = i,j
        if arr[i][j] == 'E': ex,ey = i,j

dx,dy = [-1,0,1,0],[0,1,0,-1]

from collections import deque
def BFS(sx,sy):

    deq = deque([(sx,sy,0,[])])

    visited = defaultdict(lambda:[])
    visited[(sx,sy)].append([])

    while deq:
        x,y,cnt,coins = deq.popleft()

        if x == ex and y == ey and len(coins)>=3:
            print(cnt)
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] == '#' or coins in visited[(nx,ny)]:
                continue

            visited[(nx,ny)].append(coins)
            deq.append((nx,ny,cnt+1,coins[:])) #수집을 안 할수도 있음!
            
            if arr[nx][ny] in nums: #코인이 존재, 코인을 주울 거!
                newcoin = int(arr[nx][ny])
                if len(coins)==0 or newcoin > coins[-1]: #코인이 없거나, 오름차순이거나
                    coin_ = coins[:] + [int(arr[nx][ny])]
                    deq.append((nx,ny,cnt+1,coin_))
    else:
        print(-1)

BFS(sx,sy)