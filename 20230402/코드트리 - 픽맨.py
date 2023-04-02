# 몬스터, 팩맨, 시체
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

N = 4
M,T = map(int,input().split())
R,C = map(lambda x: int(x)-1,input().split())

from collections import deque
diemonster = [[[] for _ in range(N)] for _ in range(N)]
monster = [[deque() for _ in range(N)] for _ in range(N)]
eggmonster = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,d = map(lambda x: int(x)-1, input().split())
    monster[r][c].append(d)

def first():
    '''
    몬스터 복제 시도
    '''
    global eggmonster
    eggmonster = [[deque(r) for r in row] for row in monster]

def find_direction(x,y,d):
    '''
    방향 찾아주는 함수
    '''
    for _ in range(8):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and len(diemonster[nx][ny]) == 0\
            and (nx != R or ny != C):
            return d, True
        d = (d+1)%8
    return d, False

def second():
    '''
    몬스터 이동
     ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 반시계
    '''
    global monster
    monster_ = [[deque() for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            while monster[x][y]:
                d = monster[x][y].popleft()
                d,movestatus = find_direction(x,y,d)
                if not movestatus:
                    monster_[x][y].append(d)
                else:
                    nx,ny = x+dx[d],y+dy[d]
                    monster_[nx][ny].append(d)
    monster = monster_

def third():
    '''
    팩맨 이동
    조합으로 depth == 3 
    큰 경우에만 업데이트 해주는 방식으로, 같으면 업데이트 안 해줌(우선순위가 낮으니까)
    '''
    global R,C
    px,py = [-1,0,1,0],[0,-1,0,1] #상좌하우
    dir = []
    
    def DFS(depth,r,c,die): #시작점, 몬스터 수
        global DIE, RES
        if depth == 3:
            if die > DIE:
                DIE = die
                RES = dir[:]
            return
        
        for i in range(4):
            nr = r + px[i]
            nc = c + py[i]

            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dir.append(i)
                DFS(depth+1,nr,nc,die+len(monster[nr][nc]))
                visited[nr][nc] = False
                dir.pop()
            else:
                dir.append(i)
                DFS(depth+1,nr,nc,die)
                dir.pop()

    DFS(0,R,C,0) ##상좌하우 (303)
    
    for d in RES:
        R = R + px[d]
        C = C + py[d]

        while monster[R][C]:
            monster[R][C].popleft()
            diemonster[R][C].append(3)
        monster[R][C] = deque()

def fourth():
    '''
    몬스터 시체 소멸
    '''
    global diemonster
    diemonster_ = [[[] for _ in range(N)] for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            for turn in diemonster[x][y]:
                if turn == 1:
                    continue
                diemonster_[x][y].append(turn-1)

    diemonster = diemonster_

def fifth():
    '''
    몬스터 복제 완성
    '''
    for x in range(N):
        for y in range(N):
            for d in eggmonster[x][y]:
                monster[x][y].append(d)

def simulation():
    first()
    second()
    third()
    fourth()
    fifth()

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
for _ in range(T):
    DIE, RES = -1, [] # 초기값 0으로 둬서 하나도 못 잡는 경우가 고려안 됨...!!
    visited = [[False]*N for _ in range(N)]
    simulation()

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(monster[x][y])
print(answer)