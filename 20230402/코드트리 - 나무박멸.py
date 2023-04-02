import sys
sys.stdin = open('input.txt','rt')

N,M,K,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
jaecho = [[0]*N for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]

# 총 나무의 그루 수는 1 이상 100 이하의 수로, 빈 칸은 0, 벽은 -1
def first():
    '''
    나무 성장 주변 나무 세서 그만큼 성장 
    복사할 필요 없음
    '''
    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0:
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] > 0:
                        arr[x][y] += 1

def second():
    '''
    인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식
    -> 빈칸이면서(0) 제초제가 없는 곳(0)
    배열 복사해서 진행
    '''
    global arr
    arr_ = [a[:] for a in arr]

    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and jaecho[nx][ny]==0:
                        cnt += 1
                if cnt == 0:
                    continue
                
                amount = arr[x][y]//cnt
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and jaecho[nx][ny]==0:
                        arr_[nx][ny] += amount
    arr = arr_

def count_trees(x,y):
    '''
    x,y좌표에 제초제 뿌렸을 때 박멸할 수 있는 나무 세는 함수
    대각선 방향으로 k칸만큼 전파
    도중 벽이 있거나 나무가 아얘 없는 칸 만나면 중단 -> 0보다 큰 값
    '''
    dx,dy = [1,1,-1,-1],[1,-1,1,-1]
    kill = 0

    for i in range(4):
        x_,y_ = x,y
        for _ in range(K):
            nx, ny = x_+dx[i], y_+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] <= 0:
                break
            kill += arr[nx][ny]
            x_, y_ = nx, ny
    
    kill += arr[x][y]
    return kill

def find_position():
    '''
    가장 많이 박멸할 수 있는 위치를 구하는 함수
    나무가 없는 경우도 고려해야 함
    '''
    Kill = 0
    ax = []

    for x in range(N):
        for y in range(N):
            if arr[x][y] <= 0:
                continue
            cnt = count_trees(x,y)
            if cnt == Kill:
                ax.append((x,y))
            elif cnt > Kill:
                Kill = cnt
                ax = [(x,y)]

    if len(ax) == 0:
        return -1,-1
    x,y = sorted(ax)[0]
    return x,y

def third():
    '''
    제초제 유지 기간 조절하는 함수
    0보다 큰 경우에 대해서 -1씩 하기 
    '''
    for x in range(N):
        for y in range(N):
            if jaecho[x][y] > 0:
                jaecho[x][y] -= 1

def fourth():
    '''
    C년만큼 제초제를 뿌리는 함수\\
    제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우
    새로 뿌려진 해로부터 다시 c년동안 유지
    -1,-1인 경우에 진행하지 않는다
    '''
    dx,dy = [1,1,-1,-1],[1,-1,1,-1]
    x,y = find_position()
    if x == -1 and y == -1:
        return
    for i in range(4):
        x_,y_ = x,y
        for _ in range(K):
            nx, ny = x_+dx[i], y_+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                break
            jaecho[nx][ny] = C
            x_, y_ = nx, ny
            if arr[nx][ny] <= 0:
                break
    jaecho[x][y] = C


def fifth():
    global KILL
    for x in range(N):
        for y in range(N):
            if jaecho[x][y] > 0 and arr[x][y]>=0:
                KILL += arr[x][y]
                arr[x][y] = 0

KILL = 0

def simulation():
    first()
    second()
    third()
    fourth()
    fifth()

for _ in range(M):
    simulation()
print(KILL)
