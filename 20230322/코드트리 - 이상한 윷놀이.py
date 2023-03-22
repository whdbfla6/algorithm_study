dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]

N,K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]

info = {}
for i in range(1,K+1):
    x,y,d = map(int,input().split())
    n = len(arr[x-1][y-1])
    arr[x-1][y-1].append(i)
    info[i] = (d,x-1,y-1) #방향,x,y

def flip(d):
    if d == 1 or d == 3:
        return d+1
    else:
        return d-1
    
def move_wr(k): #white,red
    
    global flag
    d,x,y = info[k]
    nx,ny = x+dx[d],y+dy[d]

    ind = arr[x][y].index(k)
    
    tmp = arr[x][y][ind:]
    if color[nx][ny] == 1: #빨간색인 경우에는 순서를 뒤집기
        tmp = tmp[::-1]
    
    for k in tmp: #좌표 업데이트 해주기
        info[k] = (info[k][0],nx,ny)
   
    arr[nx][ny] += tmp
    if len(arr[nx][ny]) >= 4: flag = True
    arr[x][y] = arr[x][y][:ind] #이동한 말들 제거해주기


def move(k): #k번째 말 이동
    d,x,y = info[k]
    nx,ny = x+dx[d],y+dy[d]
    
    if nx<0 or nx>=N or ny<0 or ny>=N or color[nx][ny] == 2: #파란색
        d = flip(d)
        info[k] = (d,x,y) #방향 전환
        nx,ny = x+dx[d], y+dy[d] #방향 바꾸고 다시 이동
        if nx<0 or nx>=N or ny<0 or ny>=N or color[nx][ny] == 2: #또 파란색이면 멈추기
            return
        else: #빨간색이나 흰색으로 이동
            move_wr(k)
    else:
        move_wr(k)

flag = False
t = 0

for t in range(1,1001):
    for i in range(1,K+1):
        move(i)
        if flag: break
    if flag: 
        print(t)
        break
else:
    print(-1)
    