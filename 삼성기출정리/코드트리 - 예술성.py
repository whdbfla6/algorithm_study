import sys
sys.stdin = open('input.txt','rt')

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
group = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]

from collections import deque
def BFS(x,y,num,gnum):

    deq = deque([(x,y)])
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    ax = []

    cnt = 0
    visited[x][y] = True

    while deq:
        x,y = deq.popleft()
        group[x][y] = gnum
        cnt += 1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
                continue

            if arr[nx][ny] != num:
                ax.append((nx,ny))
                continue

            visited[nx][ny] = True
            deq.append((nx,ny))

    return cnt, ax

answer = 0

def get_art_score():
    global answer, group, visited

    info, axes = {}, {}
    gnum = 1
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                cnt, ax = BFS(x,y,arr[x][y],gnum)
                info[gnum] = (cnt,arr[x][y])
                axes[gnum] = ax
                gnum += 1

    for g1 in range(1,gnum):
        a,c = info[g1]
        for x,y in axes[g1]:
            g2 = group[x][y]
            b,d = info[g2]

            answer += (a+b) * c * d 

    group = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

def rotate():
    center = N//2

    narr = [a[:center] for a in arr[:center]]
    narr = list(map(list,zip(*narr[::-1])))

rotate()

# get_art_score()
# print(answer)