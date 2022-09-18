from collections import defaultdict

r,c = map(int,input().split())
st = [input() for _ in range(r)]

dic = defaultdict(list)

for i in range(r):
    for j in range(c):
        dic[j].append(st[i][j])

s,e = 0,r-2
answer = 0

while s<=e:
    mid = (s+e)//2
    sets = set()
    for i in range(c):
        sets.add(''.join(dic[i][mid+1:]))
    if len(sets) < c:
        e = mid-1
    else:
        answer = mid+1
        s = mid+1
print(answer)

