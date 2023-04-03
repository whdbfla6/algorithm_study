import sys
sys.stdin = open('input.txt','rt')

N = 1
M,K = map(int,input().split())
arr = [list(map(int,input().split()))]


def first():
    minval = min(arr[0])
    for i in range(M):
        if arr[0][i] == minval: arr[0][i] += 1

def fold(k):
    global arr,N,M
    tmp = [a[:k] for a in arr]
    tmp = list(map(list,zip(*tmp[::-1])))
    
    N, M = k+1, M-k
    arr = [arr[-1][-M:]]
    arr = tmp + arr

def second():
    cnt, flag = 1, True
    while flag:
        for _ in range(2):
            if N > M-cnt:
                for i in range(N-1):
                    arr[i] = arr[i] + [0]*(M-cnt)
                return
            fold(cnt)
        cnt += 1

def third():
    global arr,N,M
    dx, dy = [1,0,-1,0],[0,1,0,-1]
    arr_ = [a[:] for a in arr]
    visited = [[False]*M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            visited[x][y] = True
            if arr[x][y] == 0:
                continue
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if nx<0 or nx>=N or ny<0 or ny>=M or arr[nx][ny] == 0 or visited[nx][ny]:
                    continue
                a, b = arr[x][y], arr[nx][ny]
                d = abs(a-b)//5
                if a > b:
                    arr_[x][y] -= d
                    arr_[nx][ny] += d
                else:
                    arr_[nx][ny] -= d
                    arr_[x][y] += d
    tmp = []
    for j in range(M):
        for i in range(N-1,-1,-1):
            if arr_[i][j] == 0:
                break
            tmp.append(arr_[i][j])
    
    N,M = 1, len(tmp)
    arr = [tmp]

def fourth():
    global arr,N,M
    for _ in range(2):
        pre = [a[:M//2][::-1] for a in arr][::-1]
        next = [a[M//2:] for a in arr]
        arr = pre + next
        N, M = N*2, M//2


def simulation():
    first()
    second()
    third()
    fourth()
    third()
    
T = 0
while True:
    simulation()
    T += 1
    minval, maxval = min(arr[0]), max(arr[0])
    if maxval - minval <= K:
        print(T)
        break

