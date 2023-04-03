# 벽, 나무, 빈칸
# 제초제

N,M,K,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
jaecho = [[0]*N for _ in range(N)]

dx,dy = [1,0,-1,0],[0,1,0,-1]
def first():
    '''
    나무 성장하는 함수\\
    배열 복사 필요 없음
    '''
    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0:
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] > 0: 
                            arr[x][y] += 1

def second():
    '''
    번식을 진행하는 함수\\
    배열 복사 필요
    빈칸, 제초제 없는 곳
    '''
    global arr
    arr_ = [a[:] for a in arr]

    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0:
                cnt = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and jaecho[nx][ny] == 0: 
                        cnt += 1
                if cnt == 0: continue
                
                amount = arr[x][y] // cnt
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0 and jaecho[nx][ny] == 0: 
                        arr_[nx][ny] += amount
    arr = arr_

def count_killed_trees(cx,cy): # 0. 그 칸에 뿌렸을 때 죽일 수 있는 나무 수 세는 함수
    dx,dy = [1,-1,1,-1],[1,1,-1,-1]
    kill = 0

    kill += max(arr[cx][cy],0) # 벽에 뿌려질 수도 있어서..?
    if kill == 0: return kill # 가운데 나무가 없는 경우
    
    for k in range(4):
        x,y = cx,cy
        for _ in range(K): # 최대 k칸 이동
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                break
            kill += max(arr[nx][ny],0)
            if arr[nx][ny] <= 0: # 벽이 있거나, 나무가 없거나
                break
            x, y = nx, ny
    return kill

def find_position(): # 1. 제초제 뿌릴 위치 찾고(최대 k칸,함수0 사용)
    jx, jy, kill = None, None, -1 # 제초제 뿌릴 위치, 죽이는 나무 수
    
    for x in range(N):
        for y in range(N):
            k = count_killed_trees(x,y) 
            if k > kill:
                kill = k
                jx, jy = x, y
    return jx, jy

def remove_jaecho(): # 2. 제초제 사라지고(-1씩)
    for x in range(N):
        for y in range(N):
            if jaecho[x][y] > 0: jaecho[x][y] -= 1

def spread(cx,cy): # 3. 새로 뿌리고
    dx,dy = [1,-1,1,-1],[1,1,-1,-1]

    jaecho[cx][cy] = C
    if arr[cx][cy] <= 0: # 나무가 하나도 없는 경우가 있을 수 있다! 일단 뿌리기는 해야 한다
        return
    
    for k in range(4):
        x,y = cx,cy
        for _ in range(K): # 최대 k칸 이동
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                break
            jaecho[nx][ny] = C
            if arr[nx][ny] <= 0: # 벽이 있거나, 나무가 없거나
                break
            x, y = nx, ny

def kill(): # 4. 나무 박멸
    global KILL, arr
    for x in range(N):
        for y in range(N):
            if jaecho[x][y] > 0 and arr[x][y] > 0:
                KILL += arr[x][y]
                arr[x][y] = 0

def third():
    '''
    0. 그 칸에 뿌렸을 때 죽일 수 있는 나무 수 세는 함수
    1. 제초제 뿌릴 위치 찾고(최대 k칸,함수0 사용)
    2. 제초제 사라지고(-1씩)
    3. 새로 뿌리고
    4. 나무 박멸
    '''
    cx,cy = find_position()
    remove_jaecho()
    spread(cx,cy)
    kill()

def simulation():
    first()
    second()
    third()

KILL = 0
for _ in range(M):
    simulation()
print(KILL)