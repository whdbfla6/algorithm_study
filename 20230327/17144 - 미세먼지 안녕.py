import copy
dx,dy = [1,0,-1,0],[0,1,0,-1]

def diffusion(): #미세먼지 확산하는 함수
    # 확산: 미세먼지, 빈칸 => 0이상
    global arr
    arr_ = copy.deepcopy(arr)

    for x in range(R):
        for y in range(C):
            if arr[x][y] > 0:
                amount = arr[x][y]//5
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<R and 0<=ny<C and arr[nx][ny]>=0:
                        arr_[x][y] -= amount
                        arr_[nx][ny] += amount
    arr = arr_

def debug():
    for a in arr:
        print(a)
    print()


def clean_clockwise():
    dir = [(0,1), (1,0), (0,-1), (-1,0)]
    x,y,d = lx,1,0
    prev = 0

    while True:
        if x == lx and y == 0:
            break
        nx = x+dir[d][0]
        ny = y+dir[d][1]
        
        if nx<0 or nx>=R or ny<0 or ny>=C: #방향전환
            d += 1
            continue
        
        arr[x][y], prev = prev, arr[x][y] # swap
        x,y = nx,ny

def clean_anti_clockwise():
    dir = [(0,1), (-1,0), (0,-1), (1,0)]
    x,y,d = ux,1,0
    prev = 0

    while True:
        if x == ux and y == 0:
            break
        nx = x+dir[d][0]
        ny = y+dir[d][1]
        
        if nx<0 or nx>=R or ny<0 or ny>=C: #방향전환
            d += 1
            continue
        
        arr[x][y], prev = prev, arr[x][y] # swap
        x,y = nx,ny


R,C,T = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

for x in range(R):
    if arr[x][0] == -1:
        ux,lx = x,x+1 #공기청정기 위치
        break

def get_dust_amount():
    amount = 2
    for x in range(R):
        for y in range(C):
            amount += arr[x][y]
    return amount


def solution():
    for _ in range(T):
        diffusion()
        clean_clockwise()
        clean_anti_clockwise()
    print(get_dust_amount())

solution()