import sys
sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def return_red():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0: visited[x][y] = False

from collections import deque
dx,dy = [1,0,-1,0],[0,1,0,-1]

def find_bomb_group(x,y,color):
    '''
    폭탄 묶음 찾기 전에 빨간 돌은 VISIT FALSE 처리하고 들어가기
    output (전체 수, 빨간색 폭탄 수, 기준점 행, 기준점 열, 좌표들) 
    '''
    global visited
    
    return_red()
    visited[x][y] = True

    deq = deque([(x,y)])
    cnt, redcnt = 1,0
    row, col = x, y # 행은 큰 값, 열은 작은 값
    ax = []

    while deq:
        x,y = deq.popleft()
        ax.append((x,y))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny] or arr[nx][ny] not in [color,0]:
                continue
            
            visited[nx][ny] = True
            cnt += 1

            if arr[nx][ny] == 0: 
                redcnt += 1
            else:
                row = max(row,nx)
                col = min(col,ny)

            deq.append((nx,ny))

    return cnt,redcnt,row,col,ax
    

def remove_bomb(ax):
    '''
    폭탄 전부 제거
    [input] 폭탄 묶음 좌표들
    '''
    for x,y in ax:
        arr[x][y] = -2

def move_down():
    '''
    빈칸 발견하는 순간 그 위에 폭탄들 전부 아래로
    근데 검은 돌을 발견하면 내려오는 작업 중지해야 함
    '''
    global arr 
    arr_ = [[-2]*N for _ in range(N)]
    
    for y in range(N):
        ind = N-1
        for x in range(N-1,-1,-1):
            if arr[x][y] == -1:
                arr_[x][y] = -1
                ind = x-1
            if arr[x][y] >= 0:
                arr_[ind][y] = arr[x][y]
                ind -= 1
    arr = arr_


def anti_clockwise():
    global arr
    arr = list(map(list,zip(*arr)))[::-1]

def debug():
    for a in arr:
        print(a)
    print()

answer = 0 
def solution():
    '''
    (전체 수, 빨간색 폭탄 수, 기준점 행, 기준점 열, 좌표들) 
    '''
    global answer
    res = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                res.append(find_bomb_group(i,j,arr[i][j]))

    if len(res) == 0:
        return False
    
    res.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
    cnt, _, _, _, ax = res[0]
    if cnt == 1:
        return False
    
    answer += cnt ** 2
    remove_bomb(ax)
    move_down()
    debug()
    
    anti_clockwise()
    debug()
    move_down()
    debug()

    return True

visited = [[False]*N for _ in range(N)]
solution()

# flag = True
# while flag:
#     visited = [[False]*N for _ in range(N)]
#     flag = solution()
# print(answer)