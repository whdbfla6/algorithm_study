import sys
sys.setrecursionlimit(10**6)

m,n,k = map(int,input().split())
paper = [[0]*n for _ in range(m)]

for _ in range(k):
    lx,ly,rx,ry = map(int,input().split())
    for i in range(m-ry,m-ly):
        for j in range(lx,rx):
            paper[i][j] = 1

visited = [[False]*n for _ in range(m)]
dx,dy = [0,1,0,-1],[1,0,-1,0]

def DFS(x,y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and paper[nx][ny]==0:
            visited[nx][ny] = True
            cnt += 1
            DFS(nx,ny)

answer = []

for i in range(m):
    for j in range(n):
        if paper[i][j]==0 and not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            DFS(i,j)
            answer.append(cnt)

answer.sort()
print(len(answer))
for x in answer:
    print(x,end=' ')