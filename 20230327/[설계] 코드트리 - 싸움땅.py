import sys
sys.stdin = open('input.txt','rt')

# 총 [공격력,위치]
# 사람[초기공격력, 총공격, 방향, 위치]

# 사람은 하나 -> 지면 이동해야 하니까
# 총도 여러 개 있을 수 있다

N,M,K = map(int,input().split())
guns = [list(map(lambda x: [int(x)],input().split())) for _ in range(N)]
players = [[0]*N for _ in range(N)] 

dx,dy = [0,0,0,0],[0,0,0,0]

def debug():
    for g in guns:
        print(g)
    print()
    for p in players:
        print(p)
    print()

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
            if players[x][y][0] == pnum:
                return x,y
    return -1,-1

def rotate(d):
    if d == 0 or d == 1:
        return d + 2
    else:
        return d - 2

def next_position(x,y,pnum):
    '''
    다음 이동 위치 구해주는 함수, 방향이 바뀌면 정보 변환
    [input] 기존위치, player number
    [output] 다음위치
    '''

    return

def get_gun(pnum):
    '''
    총 정보를 업데이트 해주는 함수
    '''

def fight(x,y,p1,p2):
    '''
    [input] 싸우는 위치, 플레이어1 번호, 플레이어2 번호
    [output] 이긴사람, 진사람 번호
    '''

def loser_action(x,y,pnum):
    '''
    [input] 싸우던 위치, 진사람 번호
    '''

def winner_action(x,y,pnum):
    '''
    [input] 싸우는 위치, 이긴 사람 번호
    '''

def move_all_player():

    for pnum in range(1,M+1):
        x,y = find_player()
        if x == -1 and y == -1:
            continue
        nx,ny = next_position(x,y,pnum)
        if players[nx][ny] == 0: #플레이어 없는 경우
            get_gun()
        else:
            p2 = players[nx][ny]
            winner, loser = fight(nx,ny,pnum,p2)
            loser_action(x,y,loser)
            winner_action(x,y,winner)
