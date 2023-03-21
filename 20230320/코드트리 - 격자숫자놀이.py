from collections import deque
r,c,k = map(int,input().split())
arr = [deque(map(int,input().split())) for _ in range(3)]
N,M = 3,3

def sorting():
    global arr,N,M
    if M>N: arr = list(map(list,zip(*arr)))
    maxlen,arr_ = 0,[]

    for row in arr:
        tmp = []
        row,kind = deque(sorted(row)),0 # kind:숫자종류
        while row:
            start,cnt = row.popleft(),0 #cnt: 각 숫자 개수
            if start == 0:
                continue
            cnt,kind = 1,kind+1 #새로운 숫자 진입
            while row:
                num = row.popleft()
                if start == num:
                    cnt += 1
                else:
                    row.appendleft(num)
                    break
            tmp.append([start,cnt])
        tmp.sort(key=lambda x: x[1])
        arr_.append(sum(tmp,[]))
        maxlen = max(kind*2,maxlen)
    for t in arr_:
        t += [0]*(maxlen-len(t))

    if M>N: 
        arr = list(map(list,zip(*arr_)))
        N = maxlen
    else: 
        arr = arr_
        M = maxlen

t = 0

while t<100:
    if N>=r and M>=c and arr[r-1][c-1] == k:
        print(t)
        break
    sorting()
    t += 1
else:
    print(-1)
