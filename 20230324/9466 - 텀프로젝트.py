import sys
sys.setrecursionlimit(10**5)

def DFS(x,team):
    global answer

    y = relation[x]
    if visited[y]:
        if y in team: answer += team[team.index(y):] #출발점 이전에 연결된 노드들은 같은 팀원이될 수 없다
        return
    
    visited[y] = True
    DFS(y,team+[y])

T = int(input())
for _ in range(T):      
    N = int(input())
    relation = [0] + list(map(int,input().split()))
    visited = [False]*(N+1)
    answer = []

    for x in range(1,N+1):
        if not visited[x]:
            visited[x] = True
            DFS(x,[x])

    print(N-len(answer))
