r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]

dx,dy = [1,0,-1,0],[0,1,0,-1]

def func(x,y):
    count = [[-1]*c for _ in range(r)]
    alphbet = set()
    count[0][0] = 1
    alphbet.add(board[0][0])
    def DFS(x,y):
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in alphbet and count[nx][ny]==-1:
                alphbet.add(board[nx][ny])
                count[nx][ny] = count[x][y] + 1
                DFS(nx,ny)
    DFS(x,y)
    answer = 1
    for i in range(r):
        for j in range(c):
            answer = max(answer,count[i][j])
    return answer

print(func(0,1))
