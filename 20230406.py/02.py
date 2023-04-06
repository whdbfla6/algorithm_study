import sys
sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

shape_info = {1:[1,4],2:[2,2],3:[2,3],4:[2,3],5:[2,3],6:[2,3],7:[2,3]}

tetris = {0:{1:[(0,0),(0,1),(0,2),(0,3)],
            2:[(0,0),(0,1),(1,0),(1,1)],
            3:[(0,1),(1,0),(1,1),(1,2)],
            4:[(0,0),(1,0),(1,1),(1,2)],
            5:[(0,1),(0,2),(1,0),(1,1)],
            6:[(0,2),(1,0),(1,1),(1,2)],
            7:[(0,0),(0,1),(1,1),(1,2)]}}

for i in range(1,4): #4방향
    tetris[i] = {i: [] for i in range(1,8)}
    for s in range(1,8): #모양
        n,m = shape_info[s]
        for x,y in tetris[i-1][s]:
            tetris[i][s].append((m-1-y,x))
        shape_info[s] = [m,n]

tetris_ax = []
for i in range(4):
    for s in range(1,8):
        t = sorted(tetris[i][s],key=lambda x: (-x[1],x[0]))
        if t not in tetris_ax:
            tetris_ax.append(t)

def get_point():
    point = 0
    for x in range(N):
        if sum(arr[x]) == M:
            point += 1
    return point

def move_down(ax):
    while True:
        newax = [(x+1,y) for x,y in ax]
        for x,y in newax:
            if x>=N:
                return ax
            if arr[x][y] == 1:
                return ax
        ax = newax

answer = 0
def move_down_all():
    global answer,arr

    for t in tetris_ax:
        for i in range(M): #i칸씩 옆으로 이동
            ax = []
            for x,y in t:
                nx, ny = x, y+i
                if ny<0 or ny>=M:
                    break
                ax.append((nx,ny))
            else:
                arr_ = [a[:] for a in arr]
                newax = move_down(ax)
                for x,y in newax:
                    arr[x][y] = 1
                answer = max(get_point(),answer)
                arr = arr_

move_down_all()
print(answer)