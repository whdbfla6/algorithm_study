from collections import deque
n,k = map(int,input().split())
leng = 100001
times = [-1]*leng

deq = deque([n])
times[n] = 0

while deq:
    pos = deq.popleft()
    if pos == k:
        print(times[k])
        exit()
    if 0<=2*pos<leng and times[2*pos] == -1:
        times[2*pos] = times[pos]
        deq.appendleft((2*pos))
    if 0<=pos+1<leng and times[pos+1] == -1:
        times[pos+1] = times[pos] + 1
        deq.append((pos+1))
    if 0<=pos-1<leng and times[pos-1] == -1:
        times[pos-1] = times[pos] + 1
        deq.append((pos-1))