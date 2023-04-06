dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]

N,K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]

for i in range(1,K+1):
    x,y,d = map(int,input().split())
    arr[x-1][y-1].append((i,d))

def find(k):
    for x in range(N):
        for y in range(N):
            for i,(j,d) in enumerate(arr[x][y]):
                if j == k:
                    return d,x,y,i

#  0은 흰색 판, 1은 빨간색 판, 2는 파란색
def flip(d):
    if d == 1 or d == 3:
        return d+1
    else:
        return d-1
    
def move_wr(k): #white,red
    
    global flag
    d,x,y,ind = find(k)
    nx,ny = x+dx[d],y+dy[d]
    
    tmp = arr[x][y][ind:]
    if color[nx][ny] == 1:
        tmp = tmp[::-1]
   
    arr[nx][ny] += tmp
    if len(arr[nx][ny]) >= 4: flag = True
    arr[x][y] = arr[x][y][:ind]


def move(k): #k번째 말 이동
    d,x,y,ind = find(k) #방향, 위치, (x,y)에서 어디에 위치하는가?
    nx,ny = x+dx[d],y+dy[d]
    
    if nx<0 or nx>=N or ny<0 or ny>=N or color[nx][ny] == 2:
        d = flip(d)
        nx,ny = x+dx[d], y+dy[d]
        arr[x][y][ind] = (k,d)
        if nx<0 or nx>=N or ny<0 or ny>=N or color[nx][ny] == 2:
            return
        else:
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