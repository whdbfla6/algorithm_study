import heapq
import math

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
pairs = []

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    pairs.append((a,b))

INF = math.inf

def dijstra(v):
    distance = [INF]*(1+N)
    distance[v] = 0

    q = []
    heapq.heappush(q,(0,v))

    while q:
        d,x = heapq.heappop(q)
        if distance[x] < d:
            continue
        for i in graph[x]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

original = dijstra(1)[N]

distance = [INF]*(1+N)
distance[0] = 0

def dijstra(v):
    global distance
    q = []
    heapq.heappush(q,(0,v))

    while q:
        d,x = heapq.heappop(q)
        if distance[x] < d:
            continue
        for i in graph[x]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance