T = int(input())
N = 4

dx,dy = [1,0,-1,0],[0,1,0,-1]

def DFS(depth,x,y,st):
    global cnt
    if depth == 7:
        if st not in allset:
            allset.add(st)
            cnt += 1
        return
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        st += arr[nx][ny]
        DFS(depth+1,nx,ny,st)
        st = st[:-1]

for t in range(1,T+1):
    cnt,allset = 0,set()
    arr = [list(input().split()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            DFS(0,i,j,'')

    print('#{} {}'.format(t,cnt))