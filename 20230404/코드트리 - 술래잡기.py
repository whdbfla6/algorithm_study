N,M,H,K = map(int,input().split()) #m 도망자 H나무 K턴

dx,dy = [-1,0,1,0],[0,1,0,-1] #위, 오, 아래, 왼
arr = [[[] for _ in range(N)] for _ in range(N)]
trees = [[0]*N for _ in range(N)]

for _ in range(M):
    x,y,d = map(int,input().split())
    arr[x-1][y-1].append(d)

for _ in range(H):
    x,y = map(int,input().split())
    trees[x-1][y-1] = 1

def swap_dir(i):
    if i == 0 or i == 1: return i+2
    else: return i-2

def first():
    '''
    도망자가 움직이는 함수
    '''
    global arr
    arr_ = [[[] for _ in range(N)] for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            dist = abs(R-x) + abs(C-y)
            if dist > 3:
                arr_[x][y] = arr[x][y][:]
                continue

            for d in arr[x][y]:
                nx,ny = x+dx[d], y+dy[d]
                if nx<0 or nx>=N or ny<0 or ny>=N: # 격자 벗어나는 경우
                    d = swap_dir(d)
                    nx,ny = x+dx[d], y+dy[d]
                
                if nx == R and ny == C: #술래가 있으면 움직이지 않는다
                    arr_[x][y].append(d)
                    continue
                arr_[nx][ny].append(d)
    arr = arr_

clock, anticlock = {}, {}

def catcher_move(): # (0,0) 방향 나중에 생각해보기
    x, y, d, cnt = N//2, N//2, 0, 1
    flag = True

    while flag:
        for _ in range(2):
            if not flag: break
            for _ in range(cnt):
                x_, y_ = x, y
                nx, ny = x+dx[d], y+dy[d]
                clock[(x,y)] = [nx,ny,d]
                x, y = nx, ny
                if x == 0 and y == 0:
                    flag = False
                    break

            d = (d+1)%4
            clock[(x_,y_)][-1] = d
        cnt += 1

    x,y,d,cnt = -1,N,3,N
    flag = True

    while flag:
        for _ in range(2):
            if not flag: break
            for _ in range(cnt):
                x_, y_ = x, y
                nx, ny = x+dx[d], y+dy[d]
                anticlock[(x,y)] = [nx,ny,d]
                x, y = nx, ny
                if x == N//2 and y == N//2:
                    flag = False
                    break

            d = (d-1)%4
            anticlock[(x_,y_)][-1] = d
        cnt -= 1
    anticlock[(N//2-1,N//2)][-1] = 0

def second():
    global clock_flag, POINT, R, C

    if clock_flag == 1:
        R,C,d = clock[(R,C)]
        if R==0 and C==0:
            clock_flag = 0
    else:
        R,C,d = anticlock[(R,C)]
        if R == N//2 and C == N//2:
            clock_flag = 1
    
    x,y = R,C

    for _ in range(3):
        if x<0 or x>=N or y<0 or y>=N:
            break
        if trees[x][y] == 0:
            POINT += len(arr[x][y]) * TURN
            arr[x][y] = []
        x, y = x+dx[d], y+dy[d]

catcher_move()

R,C = N//2, N//2
POINT, TURN = 0, 1
clock_flag = 1

def simulation():
    global TURN
    first()
    second()
    TURN += 1

for _ in range(K):
    simulation()
print(POINT)