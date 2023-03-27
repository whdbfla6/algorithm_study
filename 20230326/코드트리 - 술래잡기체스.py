def find_position(num): # 해당 번호의 말 위치
    # [아웃풋] 그 말이 존재하면 x y 아니면 -1 -1
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] == num:
                return i,j
    else:
        return -1,-1

def catch(px,py,nx,ny): #도둑말 잡는 함수
    # [인풋] 술래말 위치(px,py) 잡는말 위치(nx,ny)
    arr[px][py] = [0,0]

    _,d = arr[nx][ny] #기존 말이 갖는 방향
    arr[nx][ny] = [-1,d]

def find_direction(x,y): #움직일 수 있는 방향 찾기, 이동할 수 있는가?
    # [인풋] 그 말의 위치 -> [아웃풋] 이동 가능 여부 불리언
    _,d = arr[x][y]
    for _ in range(8):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and arr[nx][ny][0]>=0:
            arr[x][y][1] = d
            return True
        d = (d+1) % 8
    return False

def switch(x,y): # 도둑말이 이동
    _,d = arr[x][y]
    nx,ny = x+dx[d],y+dy[d] 
    arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]

def move_all(): #1~16번 말이 이동하는 함수
    for num in range(1,17):
        x,y = find_position(num)
        if x == -1 and y == -1:
            continue

        move_available = find_direction(x,y)
        if move_available:
            switch(x,y)

def init():
    global answer
    _,d = arr[0][0] #기존 말이 갖는 방향
    arr[0][0] = [-1,d]

def catch_available(px,py): #술래가 도둑을 잡을 수 있는가?
    # [인풋] 술래말 위치 [아웃풋] 잡을 수 있나?
    _,d = arr[px][py]
    for i in range(1,4):
        nx = px+dx[d]*i
        ny = py+dy[d]*i
        if 0<=nx<N and 0<=ny<N and arr[nx][ny][0] > 0:
            return True
    return False

import copy
def DFS(depth,summ):
    global answer, arr
    move_all()

    px,py = find_position(-1)
    _,pd = arr[px][py]

    if not catch_available(px,py):
        answer = max(summ,answer)
        return

    for i in range(1,4):
        nx = px+dx[pd]*i
        ny = py+dy[pd]*i

        if 0<=nx<N and 0<=ny<N and arr[nx][ny][0] > 0: 
            arr_ = copy.deepcopy(arr)
            num,_ = arr[nx][ny]
            catch(px,py,nx,ny)

            DFS(depth+1,summ+num)
            arr = arr_

N = 4
arr = [[[0,0] for _ in range(N)] for _ in range(N)]
#빈칸 [0,0] 술래 [-1,d] 말 [1~16,d]

#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dx,dy = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        num,d = tmp[j*2:j*2+2]
        arr[i][j] = [num,d-1]

answer = 0
num = arr[0][0][0]
init()
DFS(0,num)
print(answer)
