n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
x = int(input())
cnt = 0

for s in range(n-1):
    e = s+1
    summ = sum(arr[s:e+1])
    while summ<x and e<n-1:
        summ = summ - arr[e] + arr[e+1]
        e += 1
    if summ == x:
        cnt += 1

print(cnt)