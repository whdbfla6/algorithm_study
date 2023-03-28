import sys
sys.stdin = open('input.txt','rt')


N = int(input())
dx,dy = [0,-1,-1,0,1,1,1,0,-1],[0,0,-1,-1,-1,0,1,1,1]

dir_info = {}
for i in range(1,9):
    dir_info[i] = list(map(int,input().split()))

R,C = 100,4
arr = [[0]*C for _ in range(R)]

def debug():
    print('행의 개수: ', R)
    for a in arr:
        print(a)
    print()

def move_block_down(num,col):
    '''
    블록이 아래로 내려오는 함수
    내려온 후에 첫번째 행에 블록이 하나라도 생기는 경우 행 추가하기
    '''
    global R
    col -= 1
    for x in range(1,R):
        if arr[x][col] > 0:
            arr[x-1][col] = num
            break
    else:
        arr[R-1][col] = num

def get_point():
    '''
    4개의 블록이 쌓이면 점수 획득
    가장 위부터 확인하면서 블록 4개발견하면 그 윗부분 블록 하나씩 내리기
    '''
    point = 0
    flag = True

    while flag:
        flag = False
        for x in range(R-1,-1,-1):
            cnt = 0
            for y in range(C):
                if arr[x][y] > 0: 
                    cnt += 1

            if cnt == 4:
                flag = True
                arr[x] = [0]*4
                point += 1
                for nx in range(x-1,-1,-1):
                    for ny in range(C):
                        if arr[nx][ny]>0: arr[nx+1][ny],arr[nx][ny] = arr[nx][ny],0
    return point


def next_position(x,y,num):
    '''
    각 블록별로 이동하는 위치
    [output] nx,ny
    '''
    for i in dir_info[num]:
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            return nx,ny


def move_block():
    '''
    모든 블록을 이동
    배열을 복사해서 이동시키자 -> 블록의 원래 위치정보가 보존되어야 하니까!
    '''
    global arr
    arr_ = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if arr[x][y] > 0:
                nx,ny = next_position(x,y,arr[x][y])
                if arr_[nx][ny] > 0:
                    if arr[x][y] < arr_[nx][ny]:
                        arr_[nx][ny] = arr[x][y]
                else:
                    arr_[nx][ny] = arr[x][y]

    arr = arr_


def move_down():
    '''
    중력에 의해서 블록이 하나씩 아래로 내려오는 함수
    위에부터 처리(아래가 비어있으면 한칸 내리기)
    '''
    for x in range(R-1):
        for y in range(C):
            if arr[x+1][y]==0:
                for ux in range(x,-1,-1):
                    if arr[ux][y]>0:
                        arr[ux+1][y],arr[ux][y] = arr[ux][y],0

def simulation(num,col):
    move_block_down(num,col) # 블록 하나 내려옴

    point = get_point() # 4개 열 채워지는 경우 지워줌
    move_down()

    move_block() # 방향 순서에 따라 움직임
    move_down()

    point += get_point() #열이 다시 채워지는 경우 지워줌
    move_down()

    return point

answer = 0
import copy
block_info = [list(map(int,input().split())) for _ in range(N)]

def DFS(depth,summ):
    global answer,arr

    if depth == N:
        answer = max(answer,summ)
        return

    num, col = block_info[depth]

    if col == 0:
        for c in range(1,5):
            arr_ = copy.deepcopy(arr)
            point = simulation(num,c)
            DFS(depth+1,summ + point)

            arr = arr_ #원래 행렬로 만들어줌
    else:
        point = simulation(num,col)
        DFS(depth+1,summ + point)



DFS(0,0)
print(answer)