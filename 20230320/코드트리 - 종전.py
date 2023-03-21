N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dx,dy = [-1,-1,1,1],[1,-1,-1,1]

def range_check(x,y):
    return 0<=x<N and 0<=y<N

def possible(x,y,a,b):
    return range_check(x-a,y+a) and range_check(x-a-b,y+a-b) and range_check(x-b,y-b)

def border_check(x,y,a,b):
    # 경계를 True 처리
    size = [a,b,a,b] 

    for i in range(4):
        for _ in range(size[i]):
            x,y = x+dx[i],y+dy[i]
            border[x][y] = True

def make_section(x,y,a,b):
    border_check(x,y,a,b)
    cnt = [0]*5
    
    for i in range(x-a+1,N): # 하단우측
        for j in range(N-1,y-1,-1): #N-1부터 왼쪽으로 이동하면서 경계 만나면 break
            if border[i][j]: break
            cnt[4] += arr[i][j]

    for i in range(x-a+1): #상단우측
        for j in range(N-1,y+a-b,-1):
            if border[i][j]: break
            cnt[2] += arr[i][j]

    for i in range(x-b): #상단좌측
        for j in range(y+a-b+1):
            if border[i][j]: break
            cnt[1] += arr[i][j]

    for i in range(x-b,N): # 하단좌측
        for j in range(y): # 0부터 y까지 탐색하면서 경계만나면 break하자
            if border[i][j]: break
            cnt[3] += arr[i][j]
    
    cnt[0] = summ - sum(cnt) #1번구역 인구수는 전체 배열에서 나머지 구역(2~5) 인구수 빼면 구할 수 있다
    return max(cnt) - min(cnt)

answer = 10**6
summ = sum(map(sum,arr))

for x in range(N):
    for y in range(N):
        for a in range(1,N): #이동 가능한 거리는 1~N-1
            for b in range(1,N):
                if possible(x,y,a,b): #네 꼭지점이 범위안에 있는 경우에 탐색 시작
                    border = [[False]*N for _ in range(N)]
                    answer = min(answer,make_section(x,y,a,b))

print(answer)