import sys
sys.stdin = open('input.txt','rt')

N,M = 10,4
K = int(input())
info = [tuple(map(int,input().split())) for _ in range(K)]

# 블록 떨어지기 v
# 4개 차면 점수 얻고 블록 내려오기 v
# 연한블록 처리 

def debug():
    for a in arr:
        print(a)
    print()

def find_block_position(y):
    for i in range(4,N):
        if arr[i][y] == 1:
            return i-1
    return N-1

def new_block_down_red(t,x,y):
    x,y = y, M-1-x
    if t == 3:
        x = min(find_block_position(y),find_block_position(y-1))
        arr[x][y] = arr[x][y-1] = 1
    else:
        x = find_block_position(y)
        if t == 1: arr[x][y] = 1
        if t == 2: arr[x][y] = arr[x-1][y] = 1

def new_block_down_yellow(t,x,y):
    if t == 2:
        x = min(find_block_position(y),find_block_position(y+1))
        arr[x][y] = arr[x][y+1] = 1
    else:
        x = find_block_position(y)
        if t == 1: arr[x][y] = 1
        if t == 3: arr[x][y] = arr[x-1][y] = 1

def get_point():
    global POINT
    for x in range(4,N): # 무조건 위에서부터 -> 아래부터 하면 문제 생긴다..
        if sum(arr[x]) == 4: 
            arr[x] = [0]*M
            POINT += 1
            for y in range(M): 
                for ux in range(x-1,3,-1):
                    arr[ux+1][y],arr[ux][y] = arr[ux][y],arr[ux+1][y]

def light_block():
    cnt = 0
    for x in range(4,6):
        if sum(arr[x]) > 0: cnt += 1

    if cnt == 0:
        return

    for x in range(N-1,N-1-cnt,-1):
        arr[x] = [0]*M
    
    for y in range(M):
        for ux in range(N-cnt-1,3,-1):
            arr[ux+cnt][y] = arr[ux][y]
            arr[ux][y] = 0 

def count_block():
    global CNT
    for x in range(N):
        for y in range(M):
            CNT += arr[x][y]

POINT,CNT = 0,0
arr = [[0]*M for _ in range(N)]
for t,x,y in info:
    new_block_down_yellow(t,x,y)
    get_point()
    light_block()
    debug()
count_block()

arr = [[0]*M for _ in range(N)]
for t,x,y in info:
    new_block_down_red(t,x,y)
    get_point()
    light_block()
count_block()

print(POINT)
print(CNT)

