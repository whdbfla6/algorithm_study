import sys
sys.stdin = open('input.txt','rt')

# 종류: 몬스터, 팩맨, 알, 시체
# 몬스터: 방향, 위치 -> 배열
# 알: 리스트에 잠깐 저장
# 시체: 배열에 저장
# 여러개 올 수 있음 v

N = 4
monster = [[[] for _ in range(N)] for _ in range(N)] # 방향정보 포함
diemonster = [[[] for _ in range(N)] for _ in range(N)] #몇 턴이 남았는지? 

M,T = map(int,input().split())
R,C = map(lambda x: int(x)-1,input().split()) #팩맨 위치

dx,dy = [-1,-1,0,1,1,1,0,-1],[0,-1,-1,-1,0,1,1,1] # ↑, ↖, ←, ↙, ↓, ↘, →, ↗

for _ in range(M):
    r,c,d = map(lambda x: int(x)-1,input().split())
    monster[r][c].append(d)

def debug():
    print(R,C)
    for m in monster:
        print(m)
    print()
    for d in diemonster:
        print(d)
    print()

def first():
    egg = []
    for x in range(N):
        for y in range(N):
            for d in monster[x][y]:
                egg.append((x,y,d))
    return egg

def find_direction(x,y,d):

    for _ in range(8):
        nx, ny = x+dx[d], y+dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=N or (R == nx and C == ny) or len(diemonster[nx][ny]) > 0:
            d = (d+1)%8
            continue

        return nx, ny, d
    
    return x, y, d

def second():
    global monster
    monster_ = [[[] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            for d in monster[x][y]:
                nx,ny,d = find_direction(x,y,d)
                monster_[nx][ny].append(d)
    
    monster = monster_

def DFS(depth,x,y,cnt,dir):
    global eat, pdir
    if depth == 3:
        if cnt > eat:
            eat = cnt
            pdir = dir
        return
    
    for i in range(0,8,2):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        
        if visited[nx][ny]:
            DFS(depth+1,nx,ny,cnt,dir+[i])
        else:
            visited[nx][ny] = True
            DFS(depth+1,nx,ny,cnt+len(monster[nx][ny]),dir+[i])
            visited[nx][ny] = False

def third():
    global R,C
    DFS(0,R,C,0,[])
    
    for i in pdir:
        R,C = R+dx[i], C+dy[i]
        diemonster[R][C].extend([3]*len(monster[R][C]))
        monster[R][C] = []

def fourth():
    global diemonster
    diemonster_ = [[[] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            for k in diemonster[x][y]:
                if k == 1: continue
                diemonster_[x][y].append(k-1)

    diemonster = diemonster_

def fifth(egg):
    for x,y,d in egg:
        monster[x][y].append(d)

visited = [[False]*N for _ in range(N)]
eat, pdir = -1, None # 팩맨이 먹은 몬스터 수

def simulation():
    global eat, pdir
    egg = first()
    second()
    third()
    fourth()
    fifth(egg)
    eat, pdir = 0, None

for _ in range(T):
    simulation()

answer = 0
for x in range(N):
    for y in range(N):
        answer += len(monster[x][y])
print(answer)




