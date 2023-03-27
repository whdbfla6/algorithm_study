from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

dx,dy = [0,0,-1,1],[-1,1,0,0]

height = [[-1]*M for _ in range(N)]

def BFS(sx,sy,h):
    q = deque([(sx,sy)])

    minh,pos = 9, [(sx,sy)]
    visited = [[False]*M for _ in range(N)]
    visited[sx][sy] = True

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M: # 경계를 만나면 물이 채워질 수 없음
                for px,py in pos:
                    if arr[px][py] == arr[sx][sy]:
                        height[px][py] = 0
                return

            if arr[nx][ny] > h: # 시작 노드보다 높으면서 가장 낮은 높이
                minh = min(minh,arr[nx][ny])

            if not visited[nx][ny] and arr[nx][ny] <= h: # 시작노드보다 높이가 낮거나 같거나..!
                visited[nx][ny] = True
                q.append((nx,ny))
                pos.append((nx,ny))
    
    for x,y in pos: #벽의 높이까지 채워주기
        height[x][y] = minh - arr[x][y]

for i in range(N):
    for j in range(1,M-1):
        if height[i][j] == -1:
            BFS(i,j,arr[i][j])

answer = 0
for x in range(N):
    for y in range(M):
        if height[x][y] > 0 : answer += height[x][y]

print(answer)