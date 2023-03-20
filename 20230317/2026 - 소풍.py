import sys
input = sys.stdin.readline

K,N,F = map(int,input().split())
graph = [[] for _ in range(N+1)]
matrix = [[False]*(N+1) for _ in range(N+1)]

for _ in range(F):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

    matrix[a][b] = matrix[b][a] = True

