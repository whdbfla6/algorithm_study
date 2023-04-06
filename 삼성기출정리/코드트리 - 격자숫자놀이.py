from collections import deque
r,c,k = map(int,input().split())
arr = [deque(map(int,input().split())) for _ in range(3)]
N,M = 3,3

def sorting():
    global arr,N,M
    if M>N: arr = list(map(list,zip(*arr))) #열의 크기가 더 큰 경우
    
    maxlen,narr = 0,[]

    for row in arr:
        tmp = []
        row = deque(sorted(row)) # 각 행 별로 정렬
        
        while row:
            start,cnt = row.popleft(),0 # cnt: 각 숫자 개수
            if start == 0:
                continue
            cnt = 1
            while row:
                num = row.popleft()
                if start == num: #이전 숫자와 동일하면 cnt 늘려주기
                    cnt += 1
                else: #다른 경우 while문을 중지해주고 원래 배열에 넣어준다
                    row.appendleft(num)
                    break
            tmp.append([start,cnt]) #숫자, 개수
        
        tmp.sort(key=lambda x: (x[1],x[0])) # 개수를 기준으로 정렬
        maxlen = max(len(tmp)*2,maxlen) # 열의 길이를 정하기 위해

        narr.append(sum(tmp,[]))

    for row in narr:
        row += [0]*(maxlen-len(row)) # 길이가 모자라는 경우 0으로 채워주기

    if M>N: #열의 크기가 더 큰 경우
        arr = list(map(list,zip(*narr)))
        N = maxlen #행의 길이 조정하자
    else: 
        arr = narr
        M = maxlen #열의 길이 조정하자

t = 0 #시간

while t<100:
    if N>=r and M>=c and arr[r-1][c-1] == k:
        print(t)
        break
    sorting()
    t += 1
else:
    print(-1)
