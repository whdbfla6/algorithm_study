from collections import deque
N,M,k = map(int,input().split())
arr = [[0]*M for _ in range(N)]
info = {}

dx,dy = [0,-1,1,0,0],[0,0,0,1,-1]

for i in range(1,k+1):
    x,y,s,d,b = map(int,input().split())
    arr[x-1][y-1] = i
    info[i] = (s,d,b)
    
def remove(col): #채취하기
    global answer
    for i in range(N):
        if arr[i][col] > 0:
            answer += info[arr[i][col]][-1]
            arr[i][col] = 0
            break

def change_direction(n): #벽 부딪히는 경우 방향 전환
    global info
    s,i,b = info[n]
    if i == 2 or i == 4: 
        info[n] = (s,i-1,b)
        return i-1
    elif i == 1 or i == 3:
        info[n] = (s,i+1,b)
        return i+1

def move():
    global arr
    arr_ = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0: #곰팡이 존재하는 경우
                x,y = i,j #i,j값은 바뀌면 안되니까 x,y에 값 넣어주기
                n = arr[x][y]
                s,d,b = info[n] #속도,방향,크기
                for _ in range(s):
                    nx = x+dx[d]
                    ny = y+dy[d]
                    if nx<0 or nx>=N or ny<0 or ny>=M:
                        d = change_direction(n) #방향바꾸고
                        x,y = x+dx[d],y+dy[d] #다시 이동
                    else:
                        x,y = nx,ny
                if arr_[x][y] > 0: #다른 곰팡이가 존재하는 경우
                    b1 = info[arr_[x][y]][-1]
                    if b > b1: #크기가 더 큰 경우만 업데이트
                        arr_[x][y] = n
                else:
                    arr_[x][y] = n
    arr = arr_

answer = 0
for col in range(M):
    remove(col)
    move()
print(answer)