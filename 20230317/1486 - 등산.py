import math
import heapq
def func(c):
    if ord(c) >= 97:
        return ord(c)-71
    else:
        return ord(c)-65


N,M,T,D = map(int,input().split())
arr = [list(map(lambda x:func(x),input())) for _ in range(N)]

INF = math.inf
dx,dy = [1,0,-1,0],[0,1,0,-1]

def dijstra(x,y):

    distance=  [[INF]*M for _ in range(N)]
    distance[x][y] = 0
    q = []
    heapq.heappush(q,(0,x,y))

    while q:
        d,x,y = heapq.heappop(q)

        if distance[x][y] < d:
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            diff = arr[x][y]-arr[nx][ny]
            if abs(diff)>T:
                continue
            if diff >= 0:
                cost = d + 1
            else:
                cost = d + diff**2
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,nx,ny))
    return distance

answer = arr[0][0]
distance = dijstra(0,0) # (0,0) -> 다른 좌표

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        distance2 = dijstra(i,j) # (i,j) -> (0,0)
        dist = distance[i][j] + distance2[0][0]
        height = arr[i][j]
        if dist <= D and height > answer:
            answer = height


print(answer)