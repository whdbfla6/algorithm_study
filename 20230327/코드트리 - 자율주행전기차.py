# 승객, 도착지, 자동차, 빈칸
import sys
sys.stdin = open('input.txt','rt')

N,M,C = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
sx,sy = map(lambda x: int(x)-1,input().split()) #자동차의 위치

info = {}
for num in range(2,M+2):
    x1,y1,x2,y2 = map(lambda x: int(x)-1,input().split())
    info[num] = (x2,y2)
    arr[x1][y1] = num

from collections import deque

dx,dy = [1,0,-1,0],[0,1,0,-1]

def go_to_person():
    '''
    -> 가장 가까운 사람 찾는 함수\\
    [output] 사람번호, 거리\\
    '''
    global sx,sy
    deq = deque([(sx,sy,0)])
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True

    distance = None
    ax = []

    while deq:
        x,y,dist = deq.popleft()
        
        if arr[x][y] > 1 and distance == None:
            distance = dist
            ax.append((x,y))

        elif distance != None and dist > distance:
            break

        elif arr[x][y] > 1:
            ax.append((x,y))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] == 1 or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            deq.append((nx,ny,dist+1))

    if len(ax) == 0:
        return -1,-1
    x,y = sorted(ax)[0] #가장 위, 가장 왼쪽
    num = arr[x][y]

    # 현위치 바꿔주기
    sx,sy = x,y
    arr[x][y] = 0
        
    return num,distance

def go_to_destination(ex,ey):
    '''
    -> 목적지까지 승객을 데려다주는 함수 \\
    [INPUT] 승객 목적지 [OUTPUT] 이동거리 \\
    '''
    global flag,sx,sy

    deq = deque([(sx,sy,0)])
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True

    while deq:
        x,y,dist = deq.popleft()
        if x == ex and y == ey:
            sx,sy = ex,ey
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] == 1 or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            deq.append((nx,ny,dist+1))
    return -1



def ride():
    global C
    num,dist = go_to_person()
    if dist <0:
        return False
    C -= dist
    if C <= 0:
        return False

    ex,ey = info[num]
    dist = go_to_destination(ex,ey)
    if dist < 0:
        return False
    C -= dist
    if C < 0:
        return False
    C += dist * 2
    return True
    
def debug():
    print('자동차 위치: ',sx,sy)
    for a in arr:
        print(a)
    print('남은 연료: ',C)
    print()

for _ in range(M):
    flag = ride()
    if not flag:
        print(-1)
        break
else:
    print(C)



