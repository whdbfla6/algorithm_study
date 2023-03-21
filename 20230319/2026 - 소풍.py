import sys
input = sys.stdin.readline
K,N,F = map(int,input().split())
matrix = [[0]*N for _ in range(N)]

for _ in range(F):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    matrix[a][b] = matrix[b][a] = 1

def DFS(x,depth):
    global flag
    if depth == K:
        flag = False
        for r in res:
            print(r+1)
        return
    if not flag:
        return
    for y in range(x+1,N): #조합(현재 노드보다 큰 값부터 탐색)
        if visited[y]:
            continue
        for r in res: #현재 담겨있는 친구 중 누구라도 연결되어있지 않으면 탐색 중단
            if not matrix[r][y]: 
                break
        else:
            visited[y] = True
            res.append(y)
            DFS(y,depth+1)
            if not flag:
                return
            visited[y] = False
            res.pop()

flag = True
for i in range(N):
    visited = [False]*N
    res = [i]
    visited[i] = True
    DFS(i,1)
    if not flag:
        break
else:
    print(-1)