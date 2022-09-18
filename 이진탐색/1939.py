from collections import deque

n,m = map(int,input().split())
dist = [[] for _ in range(n+1)]


dist_min, dist_max = 0,0

for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a].append((b,c))
    dist[b].append((a,c))
    dist_max = max(dist_max,c)


s,e = map(int,input().split())

def bfs(target):
    q = deque([s])
    visited = [False]*(n+1)
    visited[s] = True
    while q:
        node = q.popleft()
        if node == e:
            return True
        for b,c in dist[node]:
            if not visited[b] and c >= target:
                visited[b] = True
                q.append(b)
    return False

answer = 0

while dist_min < dist_max:
    mid = (dist_min+dist_max)//2
    if bfs(mid):
        answer = mid
        dist_min = mid + 1
    else:
        dist_max = mid - 1

print(answer)



