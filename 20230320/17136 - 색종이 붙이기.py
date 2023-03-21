N = 10
papercnt = [0]*6
visited = [[False]*N for _ in range(N)]
paper = [list(map(int,input().split())) for _ in range(N)]
answer = 26

def DFS(x,y,cnt):

    global answer

    if x == N: 
        answer = min(answer,cnt)
        return
    
    if cnt >= answer:
        return
    
    if paper[x][y] == 1 and not visited[x][y]: #종이구간이면서 탐색하지 않은 경우
        for s in range(5,0,-1):
            if papercnt[s] == 5: #사용할 수 있는 종이 최대 개수는 5개
                continue
            
            flag = True
            for i in range(s):
                for j in range(s):
                    nx = x+i
                    ny = y+j
                    if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny] or not paper[nx][ny]:
                        flag = False
                        break
                if not flag: break
            
            if flag:
                papercnt[s] += 1
                for i in range(s):
                    for j in range(s):
                        nx = x+i
                        ny = y+j
                        visited[nx][ny] = True
                if ny == N-1: 
                    DFS(x+1,0,cnt+1)
                else:
                    DFS(x,ny+1,cnt+1)
                papercnt[s] -= 1 
                for i in range(s):
                    for j in range(s):
                        nx = x+i
                        ny = y+j
                        visited[nx][ny] = False
    else: #다음 좌표로 넘겨주자
        if y == N-1: #행 번호를 1 추가하자
            DFS(x+1,0,cnt)
        else: 
            DFS(x,y+1,cnt)


DFS(0,0,0)
if answer == 26:
    print(-1)
else:
    print(answer)