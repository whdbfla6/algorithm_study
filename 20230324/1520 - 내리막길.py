
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

answer = 0
dx,dy = [1,0,-1,0],[0,1,0,-1]

def DFS(x,y):
    global answer 

    if x == N-1 and y == M-1: # 종착점에 도달한 경우
        return 1
    
    if visited[x][y] >= 0: 
        # 방문한 적이 있는 길인 경우(x,y -> N-1 M-1까지의 경우의 수가 이미 저장된 상태)
        return visited[x][y]

    route = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and arr[nx][ny] < arr[x][y]:
            route += DFS(nx,ny)

    visited[x][y] = route
    return visited[x][y]

DFS(0,0)
print(visited[0][0])