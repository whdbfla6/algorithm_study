N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)] # 이동 못하면 -1, 0 빈칸, 1 베이스캠프
store = [tuple(map(lambda x: int(x)-1,input().split())) for _ in range(M)]
position = [(-1,-1) for _ in range(M)]

from collections import deque
dx,dy = [-1,0,0,1],[0,-1,1,0]

def find_store(num):
    '''
    편의점에서 역으로 출발점으로 온다
    직전에 어떤 방향에서 온 건지 저장해주기!
    '''
    def swap(d):
        if d == 0: return 3
        if d == 3: return 0
        if d == 1: return 2
        if d == 2: return 1

    ex,ey = store[num-1] # 편의점
    sx,sy = position[num-1] # 현위치
    
    deq = deque([(ex,ey,0)])
    visited = [[False]*N for _ in range(N)]
    visited[ex][ey] = True

    distance = 10**6
    next_position = []

    while deq:
        
        x,y,dist = deq.popleft() #이전위치, 현위치, 방향, 거리

        if dist > distance:
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx == sx and ny == sy:
                distance = dist+1
                next_position.append((swap(i),x,y))
                continue

            if 0<=nx<N and 0<=ny<N and arr[nx][ny] != -1 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx,ny,dist+1))

    _,nx,ny = sorted(next_position)[0]

    return nx,ny

def first():
    '''
    편의점 방향을 향해 1칸 움직이는 함수
    '''
    global FLAG
    arrived_num = 0

    for num in range(1,M+1):
        if position[num-1] == (-1,-1): #아직 격자 밖에 있는 사람
            break
        if position[num-1] == store[num-1]: #이미 편의점 도착한 사람
            arrived_num += 1
            continue

        nx,ny = find_store(num)

        if (nx,ny) == store[num-1]: #편의점에 도착하면 못 지나가게 해야 한다
            arr[nx][ny] = -1
            arrived_num += 1

        position[num-1] = (nx,ny)
    
    if arrived_num == M: # 모두 편의점에 도착한 경우
        FLAG = False

def find_base_camp(num):
    '''
    가장 가까운 베이스 캠프 찾기
    '''
    sx,sy = store[num-1]
    visited = [[False]*N for _ in range(N)]
    
    deq = deque([(sx,sy,0)])
    visited[sx][sy] = True
    distance = 10**6

    basecamp_temp = []

    while deq:
        x,y,dist = deq.popleft()
        if dist > distance:
            break
        if arr[x][y] == 1:
            distance = dist
            basecamp_temp.append((x,y))

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny] != -1:
                visited[nx][ny] = True
                deq.append((nx,ny,dist+1))

    basecamp_temp = sorted(basecamp_temp)
    x,y = basecamp_temp[0]
    return x,y

def second():
    '''
    베이스 캠프에 들어가는 함수
    '''
    global TIME
    num = TIME
    if num > M:
        return
    x,y = find_base_camp(num)
    position[num-1] = (x,y)
    arr[x][y] = -1
    
# 지나갈 수 없는 곳을 not_moved 다 담아두었다가 행동이 다 끝나면 지나갈 수 없게 표시!
TIME = 1
FLAG = True

def simulation():
    global TIME
    first() # 편의점 이동
    second() # 베이스 캠프 들어가기
    TIME += 1

while FLAG:
    simulation()
print(TIME-1)