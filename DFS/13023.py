n = int(input())
r1 = [i for i in range(1,n+1)]
r2 = [int(input()) for _ in range(n)]
visited = [False]*n

num = 0
visited[num] = True
s1,s2 = set(),set()
s1.add(r1[num])
s2.add(r2[num])
print(s1,s2)




