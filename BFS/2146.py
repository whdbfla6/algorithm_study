from collections import deque

n = int(input())
map = [list(map(int,input().split())) for _ in range(n)] 
dx,dy = [0,1,0,-1],[1,0,-1,0]
start_point = {}

def check_area(i,j,num):
    axis = deque([(i,j)])
    visited[i][j] = True
    map[i][j] = num
    
    start_point[num] = deque()

    while axis:
        x,y = axis.popleft()
        for k in range(4):
            newx = x + dx[k]
            newy = y + dy[k]
            if 0<=newx<n and 0<=newy<n and visited[newx][newy] == False:
                visited[newx][newy] = True
                if map[newx][newy] == 1:
                    map[newx][newy] = num
                    axis.append((newx,newy))


num = 1
visited = [[False]*n for _ in range(n)]

# 섬을 다른 번호로 업데이트를 해준다
for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and visited[i][j] == False:
            check_area(i,j,num)
            num += 1

answer = 100000

# 각 섬의 위치에서 출발해서 최소거리를 찾아준다
def find_dist(num):
    global answer
    
    dist = [[-1]*n for _ in range(n)]
    axis = deque([])

    for i in range(n):
        for j in range(n):
            if map[i][j] == num:
                axis.append((i,j)) 
                dist[i][j] = 0

    while axis:
        x,y = axis.popleft()
        for k in range(4):
            newx = x + dx[k]
            newy = y + dy[k]
            if 0<=newx<n and 0<=newy<n:
                if map[newx][newy] == 0 and dist[newx][newy] == -1:
                    dist[newx][newy] = dist[x][y] + 1
                    axis.append((newx,newy))
                elif map[newx][newy]>0 and map[newx][newy] != num:
                    answer = min(answer,dist[x][y])
                    return


for i in range(1,num+1):
    find_dist(i)

print(answer)
                    
