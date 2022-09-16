from collections import deque

n = int(input())
sea = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

axis = deque([])

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9: 
            sea[i][j] = 0
            axis.append((i,j))

size = 2
save = 0

def search(x,y):

    axis = deque([(x,y,0)])
    check = [[True]*n for _ in range(n)]
    check[x][y] = False
    min_dist = 1000000
    fish_list = []

    while axis:
        x,y,dist = axis.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0<=newx<=n-1 and 0<=newy<=n-1 and check[newx][newy] and size>=sea[newx][newy]: # 한번도 지나간 적이 없고 물고기 크기보다 상어가 큰 상태
                check[newx][newy] = False
                if size > sea[newx][newy] and sea[newx][newy] != 0:
                    min_dist = dist + 1
                    fish_list.append((dist+1,newx,newy))
                elif dist+1 < min_dist:
                    axis.append((newx,newy,dist+1))
    
    return fish_list

answer = 0

while axis:
    x,y = axis.popleft()
    fish_list = search(x,y)
    if len(fish_list)==0: 
        break
    else:
        fish_list.sort()
        dist,nextx,nexty = fish_list[0]
        answer += dist
        save += 1
        sea[nextx][nexty] = 0
        if save == size:
            save = 0
            size += 1
        axis.append((nextx,nexty))

print(answer)