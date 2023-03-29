# 8:50
import sys
sys.stdin = open('input.txt','rt')

dx,dy = [1,0,-1,0],[0,1,0,-1] # 아래, 오, 위, 왼

def find_line(sx,sy):
    '''
    초기화 함수
    [input] 머리사람 좌표 [output] 이동선 좌표, 사람 몇 명?
    1을 찾고 2 -> 3부터 4까지 찾아서 그 좌표를 저장
    [(1좌표),(2좌표),..,(3좌표)]

    사람존재하면 k번째, 사람 없으면 0으로 초기화
    '''
    visited = [[False]*N for _ in range(N)]

    for i in range(4):
        nx = sx+dx[i]
        ny = sy+dy[i]
        if 0<=nx<N and 0<=ny<N and tmp[nx][ny] == 2:
            x,y = nx,ny #두번째 사람 좌표
            break

    ax = [(sx,sy),(x,y)]
    arr[sx][sy] = [1,team_number]
    arr[x][y] = [2,team_number]
    visited[sx][sy] = visited[x][y] = True
    cnt = 2

    while True:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and tmp[nx][ny]>0 and not visited[nx][ny]:
                visited[nx][ny] = True
                ax.append((nx,ny))
                if 2 <= tmp[nx][ny] < 4: 
                    cnt += 1
                    arr[nx][ny] = [cnt,team_number]
                x,y = nx,ny
                break
        else: #더 이상 갈 곳이 없음
            break
    
    return ax, cnt

def move():
    '''
    총 M명인 경우 arr[M-1]은 0으로 바꿔주고 
    [-1] 좌표가 맨 앞으로 와서 -> 앞에서 M-1까지 1~M 채워주기
    '''
    for m in range(1,M+1):
        ax,cnt = team_info[m]
        x,y = ax[cnt-1]
        arr[x][y] = [0,0]
        ax = [ax[-1]] + ax[:-1]
        
        for i in range(cnt):
            x,y = ax[i]
            arr[x][y] = [i+1,m]
        
        team_info[m] = ax,cnt

def ball_position(r_num):
    '''
    [input] 라운드 번호 [output] 시작하는 위치, 방향
    '''
    # 아래, 오, 위, 왼
    r_num = r_num % (4*N)
    if r_num == 0: r_num = 4*N

    if 0<r_num<=N:
        return r_num-1, 0, 1

    if N<r_num<=2*N:
        return N-1, r_num-N-1, 2

    if 2*N<r_num<=3*N:
        return N-(r_num-2*N), N-1, 3

    if 3*N<r_num<=4*N:
        return 0, N-(r_num-3*N), 0

def throw_ball(r_num):
    '''
    가장 먼저 만나는 사람 구해서 얻은 점수 반환하는 함수
    [input] 라운드 번호 [ouput] point
    '''
    x,y,d = ball_position(r_num)
    x,y = x-dx[d],y-dy[d]
    
    point = 0
    for _ in range(N):
        x = x+dx[d]
        y = y+dy[d]
        if arr[x][y][0] > 0:
            point = arr[x][y][0] ** 2
            change_direction(arr[x][y][1])
            break

    return point


def change_direction(m):
    '''
    머리와 꼬리를 바꾸는 함수
    [input] 팀 번호
    '''
    ax,cnt = team_info[m] #팀번호-1
    ax = ax[:cnt][::-1] + ax[cnt:][::-1]
    team_info[m] = (ax,cnt)

    for i in range(cnt):
        x,y = ax[i]
        arr[x][y] = [i+1,m]

N,M,K = map(int,input().split())
tmp = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
arr = [[[0,0] for _ in range(N)] for _ in range(N)]

team_info = [[]]
team_number = 1
for x in range(N):
    for y in range(N):
        if tmp[x][y] == 1:
            team_info.append(find_line(x,y))
            team_number += 1


def debug():
    print(team_info)
    for a in arr:
        print(a)
    print()


answer = 0
for r_num in range(1,K+1):
    move()
    answer += throw_ball(r_num)
print(answer)