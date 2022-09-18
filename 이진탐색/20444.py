n,k = map(int,input().split())
s = 0 ; e =  n//2

while s <= e:
    mid = (s+e)//2
    p = mid+1
    p = p*(n-mid+1)
    if p == k:
        print('YES')
        break
    elif p <= k:
        s = mid+1
    else:
        e = mid-1
else:
    print('NO')