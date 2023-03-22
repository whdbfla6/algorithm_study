import sys

sys.stdin = open('input.txt','rt')

T = int(input())
# T = 1
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
     
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    answer,minlen,ax = 0,10**6,[]
 
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0:
                continue
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    break
            else:
                ax.append((x,y))
 
    visited = [[False]*N for _ in range(N)]
    M = len(ax)
 
    def DFS(depth,cnt,line):
        global answer,minlen
 
        if depth == M:    
            if cnt > answer: # 현재 연결된 노드보다 개수가 많은 경우
                answer = cnt
                minlen = line
            elif cnt == answer: # 현재 연결된 노드 수와 같을 때는 선의 길이를 더 작은 값으로 업데이트
                if line < minlen: minlen = line
            return
        
        if (M-depth) + cnt < answer: 
            # 앞으로 검사해야 하는 노드와 현재 연결된 노드를 더했을 때 answer보다 작으면 실행 중단
            # answer: 최대 연결 노드 수
            return
 
        for i in range(4):
            x,y = ax[depth]
            flag,l = False,0 #전선의 길이
            while True:
                x,y = x+dx[i],y+dy[i]
                if x<0 or x>=N or y<0 or y>=N: #경계에 도달 = 연결에 성공함
                    flag = True
                    break
                l += 1
                if arr[x][y] == 1 or visited[x][y]:
                    break
            if flag: #경계에 도달한 경우
                x,y = ax[depth]
                for _ in range(l):
                    x,y = x+dx[i],y+dy[i]
                    visited[x][y] = True
                DFS(depth+1,cnt+1,line+l)
                for _ in range(l): #백트랙킹
                    visited[x][y] = False
                    x,y = x-dx[i],y-dy[i]
            else: #연결실패
                DFS(depth+1,cnt,line)
    if ax:
        DFS(0,0,0)
    else:
        minlen = 0
    print(f'#{t} {minlen}')