import sys
sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]


dx,dy = [0,1,0,-1],[1,0,-1,0] #오,아래,왼,위

dice = [[4,6,3,1],[2,5]]

def rotate_dice(dir):
    if dir == 0: 
        dice[0] = dice[0][1:] + [dice[0][0]]
    elif dir == 2:
        dice[0] = [dice[0][-1]] + dice[0][:-1]
    elif dir == 1:
        a,b = dice
        dice[1] = [a[3],a[1]]
        dice[0][1],dice[0][3] = b[0], b[1]
    else:
        a,b = dice
        dice[1] = [a[1],a[3]]
        dice[0][1], dice[0][3] = b[1], b[0]

from collections import deque
def find_area(x,y):
    '''
    상하좌우로 인접하며 같은 숫자가 적혀있는 모든 칸의 합 구하는 함수
    [input] 시작점
    '''
    point = 0
    num = arr[x][y]
    visited = [[False]*N for _ in range(N)]

    deq = deque([(x,y)])
    visited[x][y] = True

    while deq:
        x,y = deq.popleft()
        point += num

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == num and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx,ny))

    return point

def swap(d):
    if d == 0 or d == 1:
        return d + 2
    else:
        return d - 2

x,y,d = 0,0,0
answer = 0

for _ in range(M):
    nx,ny = x+dx[d], y+dy[d]
    if nx<0 or nx>=N or ny<0 or ny>=N:
        d = swap(d)
        x,y = x+dx[d], y+dy[d]
    else:
        x,y = nx,ny

    rotate_dice(d)
    answer += find_area(x,y)

    num = dice[0][1]
    if num > arr[x][y]:
        d = (d+1)%4
    elif num < arr[x][y]:
        d = (d-1)%4

print(answer)