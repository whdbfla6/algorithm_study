import sys
from collections import defaultdict
sys.stdin = open('input.txt','rt')

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
wind = [[0]*N for _ in range(N)]
wallinfo = defaultdict(lambda: False)

for _ in range(M):
    x,y,s = map(int,input().split())
    x,y = x-1, y-1
    if s == 0:
        nx,ny = x-1,y
    else:
        nx,ny = x,y-1
    
    wallinfo[(x,y,nx,ny)] = True
    wallinfo[(nx,ny,x,y)] = True


dx,dy = [0,-1,0,1],[-1,0,1,0] #왼, 위, 오, 아래

def in_range(x,y,nx,ny):
    return 0<=nx<N and 0<=ny<N and not wallinfo[(x,y,nx,ny)]

def blow(x,y,d):
    '''
    [input] 바람 위치
    '''
    ax = [(x,y)]

    for w in range(5,0,-1):

        newax = []
        for x,y in ax:
            
            x1,y1 = x+dx[d], y+dy[d]
            if in_range(x,y,x1,y1):
                newax.append((x1,y1))
                wind[x1][y1] += w

        ax = []
        for x,y in newax:
            if (x,y) not in ax: ax.append((x,y))

            nx,ny = x+dx[(d-1)%4], y+dy[((d-1)%4)]
            if (nx,ny) not in ax and in_range(x,y,nx,ny): ax.append((nx,ny))

            nx,ny = x+dx[(d+1)%4], y+dy[((d+1)%4)]
            if (nx,ny) not in ax and in_range(x,y,nx,ny): ax.append((nx,ny))

        
def mix_wind():
    '''
    인접한 칸 탐색하면서 벽이 있는지 보기
    배열 복사해서 사용하기 : 이용해보자!
    '''
    global wind
    wind_ = [a[:] for a in wind]

    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N or wind[x][y] <= wind[nx][ny] or wallinfo[(x,y,nx,ny)]:
                    continue
                
                diff = (wind[x][y] - wind[nx][ny]) // 4
                wind_[x][y] -= diff
                wind_[nx][ny] += diff
                
    wind = wind_


def wind_decrease():
    '''
    0이하면 감소하지 않는다
    '''

    for x in range(1,N-1):
        if wind[0][x] > 0: wind[0][x] -= 1
        if wind[-1][x] > 0: wind[-1][x] -= 1
        if wind[x][0] > 0: wind[x][0] -= 1
        if wind[x][-1] > 0: wind[x][-1] -= 1

    if wind[0][0] >0: wind[0][0] -= 1
    if wind[0][-1] >0: wind[0][-1] -= 1
    if wind[-1][0] >0: wind[-1][0] -= 1
    if wind[-1][-1] >0: wind[-1][-1] -= 1

def blow_all():
    for x in range(N):
        for y in range(N):
            if arr[x][y] >= 2:
                blow(x,y,arr[x][y]-2)

def check():
    '''
    사무실의 시원함이 k이상인지 확인하는 함수
    '''
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                if wind[x][y] < K: 
                    return False
    return True # 모두 k이상
    

def simulation():
    global flag
    
    blow_all()
    mix_wind()
    wind_decrease()
    return check()

def solution():
    time = 0
    for _ in range(100): 
        flag = simulation()
        time += 1
        if flag:
            print(time)
            break
    else:
        print(-1)

solution()



