import sys
sys.stdin = open('input.txt','rt')

N = int(input())
arr = [list(input()) for _ in range(N)]

for x in range(N):
    for y in range(N):
        if arr[x][y] == 'B': 
            R,C = x,y
            arr[x][y] = '.'

dx,dy = [1,0,-1,0],[0,1,0,-1]

from collections import deque

def BFS(x,y,turn):
    '''
    몸이 커지는 함수 -> 부딪히는지 아닌지 알려준다
    '''
    deq = deque([(x,y,0)])
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True

    while deq:
        x,y,t = deq.popleft()
        
        if t == turn+1:
            return True
        
        if t == turn:
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] == '#':
                return False
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            deq.append((nx,ny,t+1))
    return True

answer = 0
def DFS(x,y,turn):
    global answer
    answer = max(answer,turn)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny] == '#':
            continue
        if not BFS(nx,ny,turn):
            continue
        else:
            DFS(nx,ny,turn+1)


DFS(R,C,1)
print(answer)