from collections import deque
from itertools import combinations


n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 섬 구분
def find_area(i,j,num):
    axis = deque([(i,j)])
    visited[i][j] = True
    map[i][j] = num

    while axis:
        x,y = axis.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if map[nx][ny] == 1: 
                    map[nx][ny] = num
                    visited[nx][ny] = True
                    axis.append((nx,ny))
        
visited = [[False]*m for _ in range(n)]
num = 1
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and not visited[i][j]:
            find_area(i,j,num)
            num += 1

# 최소 거리 찾기
dist_btw_area =  [[10000]*(num) for _ in range(num)]

def find_dist(num):

    def search(x,y,k,num):
        q = deque([(x,y)])
        while q:
            x,y = q.popleft()
            nx = x + dx[k] ; ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if map[nx][ny] == num:
                    return
                if map[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
                if map[nx][ny]>0 and map[nx][ny] != num:
                    next_area = map[nx][ny]
                    d = min(dist[x][y],dist_btw_area[num][next_area])
                    if d >= 2:
                        dist_btw_area[num][next_area] = d
                        dist_btw_area[next_area][num] = d
                    return 

    for i in range(n):
        for j in range(m):
            if map[i][j] == num: 
                dist = [[-1]*m for _ in range(n)]
                dist[i][j] = 0
                for k in range(4):
                    search(i,j,k,num)  
    
for i in range(1,num):
    find_dist(i)

for x in map:
    print(x)

for x in dist_btw_area:
    print(x)


comb = list(combinations(range(1,num),2))
ans = 10000

for c in list(combinations(comb,num-2)):
    min_dist = 0
    ch = [False]*(num-1)
    for x in c:
        if ch[x[0]-1] == ch[x[1]-1] == True:
            break
        ch[x[0]-1] = True; ch[x[1]-1] = True
        d = dist_btw_area[x[0]][x[1]]
        if d == 10000:
            break
        else:
            min_dist += d
    else:
        if ch == [True]*(num-1) : 
            print(c)
            ans = min(ans,min_dist)

if ans == 10000:
    ans = -1

print(ans)




