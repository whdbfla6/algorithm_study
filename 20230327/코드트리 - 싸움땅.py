import sys
sys.stdin = open('input.txt','rt')

# 총 [공격력,위치]
# 사람[초기공격력, 총공격, 방향, 위치]

# 사람은 하나 -> 지면 이동해야 하니까
# 총도 여러 개 있을 수 있다

def func(x):
    x = int(x)
    if x == 0:
        return []
    else:
        return [x]

N,M,K = map(int,input().split())
guns = [list(map(lambda x: func(x),input().split())) for _ in range(N)]
players = [[0]*N for _ in range(N)]

dx,dy = [-1,0,1,0],[0,1,0,-1]

pinfo = {}
for pnum in range(1,M+1):
    x,y,d,s = map(int,input().split())
    players[x-1][y-1] = pnum
    pinfo[pnum] = [s,0,d] # 초기공격, 총공격, 방향

def find_player(pnum):
    '''
    [input] player number
    [output] player position
    '''
    for x in range(N):
        for y in range(N):
            if players[x][y] == pnum:
                return x,y
    return -1,-1

def rotate(d):
    if d == 0 or d == 1:
        return d + 2
    else:
        return d - 2

def next_position(x,y,pnum):
    '''
    다음 이동 위치 구해주는 함수, 방향이 바뀌면 정보 변환, 기존 위치도 0으로 바꿔준다
    [input] 기존위치, player number
    [output] 다음위치
    '''
    _,_,d = pinfo[pnum]
    nx = x+dx[d]
    ny = y+dy[d]

    if 0<=nx<N and 0<=ny<N:
        players[x][y] = 0
        return nx,ny
    
    d = rotate(d)
    pinfo[pnum][-1] = d

    nx = x+dx[d]
    ny = y+dy[d]
    players[x][y] = 0
    
    return nx,ny


def get_gun(x,y,pnum):
    '''
    총 정보를 업데이트 해주는 함수
    '''
    guncnt = guns[x][y]
    if len(guncnt) == 0: #그 자리에 총이 없는 경우
        return
    
    pregun = pinfo[pnum][1]
    newgun = max(guns[x][y])

    if pregun == 0: #내가 소지한 총이 없는 경우
        pinfo[pnum][1] = newgun
        guns[x][y].remove(newgun)
    
    elif newgun > pregun:
        pinfo[pnum][1] = newgun
        guns[x][y].remove(newgun)
        guns[x][y].append(pregun)


point = [0]*M
def fight(p1,p2):
    '''
    [input] 싸우는 위치, 플레이어1 번호, 플레이어2 번호
    [output] 이긴사람, 진사람 번호
    '''
    global point
    s1,g1,_ = pinfo[p1] 
    s2,g2,_ = pinfo[p2]

    diff = abs(s1+g1-s2-g2)

    if (s1+g1,s1) > (s2+g2,s2):
        point[p1-1] += diff
        return p1,p2
    else:
        point[p2-1] += diff
        return p2,p1
    

def loser_action(x,y,pnum):
    '''
    [input] 싸우던 위치, 진사람 번호
    '''
    if pinfo[pnum][1] > 0: # 총 버리기
        guns[x][y].append(pinfo[pnum][1])
        pinfo[pnum][1] = 0
    
    _,_,d = pinfo[pnum]

    for _ in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N and players[nx][ny] == 0:
            pinfo[pnum][-1] = d # 방향 정보 업데이트
            players[nx][ny] = pnum #이전 위치는 승자로 채워질 것
            get_gun(nx,ny,pnum)
            return
        
        d = (d+1)%4

def winner_action(x,y,pnum):
    '''
    [input] 싸우는 위치, 이긴 사람 번호
    '''
    get_gun(x,y,pnum) #총 줍기


def move_all_player():

    for pnum in range(1,M+1):
        x,y = find_player(pnum)
        if x == -1 and y == -1:
            continue
        
        nx,ny = next_position(x,y,pnum)

        if players[nx][ny] == 0: #플레이어 없는 경우
            players[nx][ny] = pnum
            get_gun(nx,ny,pnum)
        
        else:
            p2 = players[nx][ny]
            winner, loser = fight(pnum,p2)
            loser_action(nx,ny,loser)
            players[nx][ny] = winner #싸우던 위치는 승자가 차지!
            winner_action(nx,ny,winner)


for _ in range(K):
    move_all_player()

print(' '.join(map(str,point)))