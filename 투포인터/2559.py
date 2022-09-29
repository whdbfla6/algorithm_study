n,k = map(int,input().split())
arr = list(map(int,input().split()))
summ = sum(arr[:k])
maxval = summ

for s in range(n-k):
    summ -= arr[s]
    summ += arr[s+k]
    if summ > maxval:
        maxval = summ

print(maxval)