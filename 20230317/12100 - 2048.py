N = int(input())
block = [list(map(int,input().split())) for _ in range(N)]

dx,dy = [-1,0,0,1],[0,-1,1,0] 
answer = 0

def DFS(depth):

    global answer,block

    if depth == 10:
        for i in range(N):
            for j in range(N):
                answer = max(answer,block[i][j])
        return

    axis = []

    for i in range(N):
        for j in range(N):
            if block[i][j] > 0: axis.append((i,j,block[i][j]))
    
    for k in range(4):
        if k == 2: axis = sorted(axis,key = lambda x: -x[1])
        elif k == 3: axis = sorted(axis,key = lambda x: -x[0])
        else: axis = sorted(axis)
        
        status = [[False]*N for _ in range(N)] #합쳐진 블록인가?

        for x,y,number in axis:
            while True:
                nx = x+dx[k]
                ny = y+dy[k]
                if 0<=nx<N and 0<=ny<N:
                    if block[nx][ny] == number and not status[nx][ny]:
                        block[x][y],block[nx][ny] = 0, number*2
                        status[nx][ny] = True
                        break
                    elif block[nx][ny] == 0:
                        block[x][y],block[nx][ny] = 0,number
                        x,y = nx,ny
                    else: #더이상 이동 불가(다른숫자,이미합쳐진상태)
                        break
                else: #벽인경우
                    break
        DFS(depth+1)
        block = [[0]*N for _ in range(N)]
        for x,y,number in axis:
            block[x][y] = number

DFS(0)
print(answer)