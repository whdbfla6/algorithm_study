import sys
sys.stdin = open('input.txt','rt')


def time_change():
    '''
    독점 땅 시간 조정해주는 함수
    '''
    for x in range(N):
        for y in range(N):
            pnum,time = monopoly[x][y]
            if pnum>0:
                time -= 1
                if time == 0: monopoly[x][y] = [0,0]
                else: monopoly[x][y] = [pnum,time]


def find_player(pnum):
    '''
    [input] player number
    [output] x,y
    '''
    for x in range(N):
        for y in range(N):
            a,b = monopoly[x][y]
            if a == pnum and b == K:
                return x,y
    return -1,-1


import copy

diecnt = 0


def move_player():
    global diecnt

    global monopoly
    monopoly_ = copy.deepcopy(monopoly)

    for pnum in range(1,M+1):
        x,y = find_player(pnum)
        if x == -1 and y == -1:
            continue
        dir = dirinfo[pnum][curdir[pnum-1]]

        flag = False
        for i in dir: # 빈 칸 찾기
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and monopoly[nx][ny][0] == 0:
                flag = True
                curdir[pnum-1] = i
                if monopoly_[nx][ny][0] > 0: #이미 독점한 사람 존재하는 경우
                    diecnt += 1
                    if pnum < monopoly_[nx][ny][0]: #작은 번호인 경우에만 바꾸기
                        monopoly_[nx][ny] = [pnum,K+1]
                else:
                    monopoly_[nx][ny] = [pnum,K+1]
                break

        if not flag: #내가 독점한 땅
            for i in dir:
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<N and monopoly[nx][ny][0] == pnum:
                    curdir[pnum-1] = i
                    monopoly_[nx][ny] = [pnum,K+1] #내가 독점한 땅이니 나만 갈 수 있음
                    break

    monopoly = monopoly_


def debug():
    print(curdir)
    for m in monopoly:
        print(m)
    print()

dx,dy = [-1,1,0,0],[0,0,-1,1] #위, 아래, 왼쪽, 오른쪽

N,M,K = map(int,input().split())
monopoly = [[[0,0] for _ in range(N)] for _ in range(N)]

pos = [list(map(int,input().split())) for _ in range(N)]
curdir = list(map(lambda x: int(x)-1,input().split()))

for i in range(N):
    for j in range(N):
        pnum = pos[i][j]
        if pnum > 0: 
            monopoly[i][j] = [pnum,K]

dirinfo = {i:{j:[] for j in range(4)} for i in range(1,M+1)}

for i in range(1,M+1):
    for j in range(4):
        dirinfo[i][j] = list(map(lambda x: int(x)-1,input().split()))

time = 0

while True:
    move_player()
    time_change()
    time += 1
    if time > 1000:
        print(-1)
        break
    if diecnt == M-1:
        print(time)
        break
