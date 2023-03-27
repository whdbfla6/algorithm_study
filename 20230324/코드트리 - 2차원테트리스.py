import sys
sys.stdin = open('input.txt','rt')

K = int(input())
blockinfo = [tuple(map(int,input().split())) for _ in range(K)]
answer = 0

def get_block_pos(x,y,t):

    pos = [(x,y)]

    if t == 1: return pos
    if t == 2: return pos + [(x,y+1)]
    if t == 3: return pos + [(x+1,y)]

def find_block(y):
    for x in range(4,N):
        if arr[x][y] > 0:
            return x-1
    return N-1
        
def move_down(num):
    for x in range(N-1,3,-1):
        for y in range(M):
            if arr[x][y]:
                arr[x+num][y] = 1 #num칸만큼 밑에서부터 내리기
                arr[x][y] = 0

def four_row():
    global answer 
    for x in range(4,N):
        if sum(arr[x]) == M:
            arr[x] = [0]*M
            answer += 1
            for x_ in range(x-1,3,-1):
                for y in range(M):
                    if arr[x_][y]:
                        arr[x_+1][y] = 1
                        arr[x_][y] = 0

def move(x,y,t,color='yellow'):
    pos = get_block_pos(x,y,t)

    if color == 'red':
        pos = [(y,M-x-1) for x,y in pos]
        if t == 2: t = 3
        elif t == 3: t = 2

    pos = sorted(pos,key=lambda x: -x[0])

    
    if t != 2:
        for _,y in pos:
            x = find_block(y)
            arr[x][y] = 1
    else:
        x = 9
        for _,y in pos:
            x = min(x,find_block(y))
        for _,y in pos:
            arr[x][y] = 1

    four_row()
    
    special = set()
    for x in range(4,6):
        for y in range(M):
            if arr[x][y]: special.add(x)

    if special:
        deletednum = len(special)
        for x in range(N-1,N-deletednum-1,-1):
            for y in range(4):
                arr[x][y] = 0
        move_down(deletednum)


N,M = 10,4
blockn = 0

arr = [[0]*M for _ in range(N)] #빈블록
for t,x,y in blockinfo:
    move(x,y,t)
    for a in arr[4:]:
        print(a)
    print()
for a in arr[4:]:
    blockn += sum(a)

arr = [[0]*M for _ in range(N)] #빈블록
for t,x,y in blockinfo:
    move(x,y,t,color='red')


for a in arr[4:]:
    blockn += sum(a)

print(answer)
print(blockn)


