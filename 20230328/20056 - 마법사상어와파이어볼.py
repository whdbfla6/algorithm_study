import sys
sys.stdin = open('input.txt','rt')

# 위치, 질량, 방향, 속력
# 종류: 빈칸, 파이어볼
# 파이어볼 한 칸에 여러개 => (x,y) 리스트로 구성하자

dx,dy = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
N,M,K = map(int,input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,m,s,d = map(int,input().split())
    arr[x-1][y-1].append([m,s,d])

def debug():
    for a in arr:
        print(a)
    print()

def next_position(x,y,d,s): 
    '''
    방향 di로 속력 si칸 만큼 이동
    [input] 방향 속력 [output] 다음 좌표
    '''
    nx = x+dx[d]*s
    ny = y+dy[d]*s
    
    return nx%N, ny%N

def move_fireball():
    '''
    파이어볼 움직이는 함수
    기존 위치 정보를 알기 위해서 빈 배열로 이동시키자
    '''
    global arr
    arr_ = [[[] for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for m,s,d in arr[i][j]:
                nx,ny = next_position(i,j,d,s)
                arr_[nx][ny].append([m,s,d])
    arr = arr_

def combine_fireball(x,y):
    '''
    x,y 좌표에 있는 파이어볼 하나로 합치는 함수
    '''
    msum,ssum,cnt = 0,0,0

    remain = arr[x][y][0][-1] % 2 # 첫번째 파이어볼 방향
    flag = True

    for m,s,d in arr[x][y]:
        msum += m
        ssum += s
        cnt += 1
        if remain != d % 2: # 방향의 나머지가 다른 경우
            flag = False

    newm, news = msum//5, ssum//cnt
    arr[x][y] = [] # 일단 빈 배열로 만들어주고 -> 새로운 파이어볼 4개로 채워주기

    if newm == 0: # 질량이 0인 파이어볼은 소멸되어 없어진다
        return
    
    dlist = [1,3,5,7]
    if flag:  
        dlist = [0,2,4,6]
    
    for newd in dlist:
        arr[x][y].append([newm,news,newd])


def combine_all_fireball():
    '''
    모든 좌표의 파이어볼 합치는 함수
    위치 정보가 바뀌는 것이 아니라 배열 복사는 필요 없음
    '''
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2: #파이어볼 두 개 이상 존재
                combine_fireball(i,j)

def solution():
    for _ in range(K):
        move_fireball()
        combine_all_fireball()

    answer = 0
    for i in range(N):
        for j in range(N):
            for m,_,_ in arr[i][j]:
                answer += m
    print(answer)

solution()