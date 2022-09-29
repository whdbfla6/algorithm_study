n,m = map(int,input().split())
arr = list(map(int,input().split()))
summ,e = 0,0
cnt = 0

for s in range(n):
    while summ < m and e<n:
        summ += arr[e]
        e += 1
    if summ == m: cnt += 1
    summ -= arr[s]

print(cnt)