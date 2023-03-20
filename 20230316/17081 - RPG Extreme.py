N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

#만약 함정 위에서 입력받은 커맨드 방향으로 움직일 수 없어 제자리에 멈추는 경우, 해당 함정을 또 밟은 것이 된다
dir = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
moveorder = list(input())

K,L = 0,0 #몬스터 수, 아이템 수
for i in range(N):
    for j in range(M):
        if arr[i][j] == '@': 
            sx,sy = i,j
            arr[sx][sy] = '.'
        if arr[i][j] == '&': K += 1
        if arr[i][j] == 'B': L += 1

K += 1 #대왕몬스터
monsterinfo = {}
for _ in range(K):
    R,C,S,W,A,H,E = input().split()
    R,C,W,A,H,E = map(int,[R,C,W,A,H,E])
    monsterinfo[(R-1,C-1)] = (S,W,A,H,E) #위치: 이름,공격,방어,최대체력,얻는 경험치(죽일 때)

iteminfo = {}
for _ in range(L):
    R,C,T,S = input().split()
    if T in ['W','A']: R,C,S = map(int,[R,C,S])
    else: R,C = map(int,[R,C])
    iteminfo[(R-1,C-1)] = (T,S) #위치 : 무기이름 ,(W:공격력,A:방어력,O:장신구)

def get_item(R,C):
    global arr,myW,myA,Olist
    T,S = iteminfo[(R,C)] #무기이름
    if T == 'W': #무기
        myW = S
    elif T == 'A': #방어구
        myA = S
    elif len(Olist)<4:
        Olist.add(S)
    arr[R][C] = '.'

def trap():
    global HP,flag
    if 'DX' in Olist: 
        HP -=1
    else:
        HP -= 5 #데미지 5
    if HP <= 0: flag = 0

def attack_monster(R,C):
    global HP,arr,flag,x,y,EX

    _,W,A,H,E = monsterinfo[(R,C)] #이름,공격,방어,최대체력,얻는 경험치(죽일 때)
    if arr[R][C] == 'M' and 'HU' in Olist:
        HP = maxHP
    AT_ = AT + myW #임시 공격력
    DF_ = DF + myA #임시 방어력
    firstattack,firstattack2 = True,True
    while True:
        if firstattack:
            firstattack = False
            if 'CO' in Olist and 'DX' in Olist:
                H -= max(1,AT_*3 - A)
            elif 'CO' in Olist: 
                H -= max(1,AT_*2 - A)
            else:
                H -= max(1,AT_-A)
        else:
            H -= max(1,AT_ - A) # HP 내 체력, H 몬스터 체력
        if H <= 0: break
        if firstattack2:
            firstattack2 = False
            if arr[R][C] == 'M' and 'HU' in Olist:
                continue
        HP -= max(1,W-DF_)
        if HP <= 0: break

    if H<=0: #몬스터 죽임
        if 'HR' in Olist: 
            HP = min(maxHP,HP+3)
        if 'EX' in Olist: 
            EX += int(E*1.2)
        else:
            EX += E
        if arr[R][C] == 'M':
            flag = 2
        arr[R][C] = '.'
    elif HP<=0: #내가 죽음
        flag = 0

myW,myA,Olist = 0,0,set() #무기(공격력),방어구(방어력),장신구(효과를 가진 장신구 이름들)
HP,maxHP,AT,DF,EX = 20,20,2,2,0 #체력,최대체력,공격력,방어력,경험치
flag = 1 #1: 게임 진행중, 0: 사망, 2:보스 물리침

x,y = sx,sy
Turn,level = 0,1

def death():
    global x,y
    if flag == 0 and 'RE' in Olist: # 죽음
        flag = 1
        HP = maxHP
        x,y = sx,sy
        Olist.remove('RE')
    elif flag == 0 or flag == 2:
        if flag == 2:
            message = 'YOU WIN!'
            arr[nx][ny] = '@'
        elif arr[nx][ny] == '^': 
            message = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
        elif arr[nx][ny] in ['&','M']: 
            message = 'YOU HAVE BEEN KILLED BY {}..'.format(monsterinfo[(nx,ny)][0])
        for a in arr:
            print(''.join(a))
        if HP<0: HP = 0
        print('Passed Turns : {}'.format(Turn))
        print('LV : {}'.format(level))
        print('HP : {}/{}'.format(HP,maxHP))
        print('ATT : {}+{}'.format(AT,myW))
        print('DEF : {}+{}'.format(DF,myA))
        print('EXP : {}/{}'.format(EX,5*level))
        print(message)

for m in moveorder:
    nx,ny = x+dir[m][0],y+dir[m][1]
    Turn += 1
    if nx<0 or nx>=N or ny<0 or ny>=M or arr[nx][ny] == '#':
        if arr[x][y] == '^': 
            trap()
            if flag == 0 and 'RE' in Olist: # 죽음
                flag = 1
                HP = maxHP
                x,y = sx,sy
                Olist.remove('RE')
                continue
            elif flag == 0:
                message = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
                for a in arr:
                    print(''.join(a))
                if HP<0: HP = 0
                print('Passed Turns : {}'.format(Turn))
                print('LV : {}'.format(level))
                print('HP : {}/{}'.format(HP,maxHP))
                print('ATT : {}+{}'.format(AT,myW))
                print('DEF : {}+{}'.format(DF,myA))
                print('EXP : {}/{}'.format(EX,5*level))
                print(message)
                break
        continue
    elif arr[nx][ny] == 'B':
        get_item(nx,ny)
    elif arr[nx][ny] == '^':
        trap()
    elif arr[nx][ny] in ['&','M']:
        attack_monster(nx,ny)

    if EX >= 5*level:
        level += 1
        maxHP += 5
        AT,DF = AT+2, DF+2
        HP = maxHP
        EX = 0
    if flag == 0 and 'RE' in Olist: # 죽음
        flag = 1
        HP = maxHP
        x,y = sx,sy
        Olist.remove('RE')
        continue
    elif flag == 0 or flag == 2:
        if flag == 2:
            message = 'YOU WIN!'
            arr[nx][ny] = '@'
        elif arr[nx][ny] == '^':
            message = 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
        elif arr[nx][ny] in ['&','M']: 
            message = 'YOU HAVE BEEN KILLED BY {}..'.format(monsterinfo[(nx,ny)][0])
        for a in arr:
            print(''.join(a))
        if HP<0: HP = 0
        print('Passed Turns : {}'.format(Turn))
        print('LV : {}'.format(level))
        print('HP : {}/{}'.format(HP,maxHP))
        print('ATT : {}+{}'.format(AT,myW))
        print('DEF : {}+{}'.format(DF,myA))
        print('EXP : {}/{}'.format(EX,5*level))
        print(message)
        break
    x,y = nx,ny
else:
    arr[x][y] = '@'
    for a in arr:
        print(''.join(a))
    if HP<0: HP = 0
    print('Passed Turns : {}'.format(Turn))
    print('LV : {}'.format(level))
    print('HP : {}/{}'.format(HP,maxHP))
    print('ATT : {}+{}'.format(AT,myW))
    print('DEF : {}+{}'.format(DF,myA))
    print('EXP : {}/{}'.format(EX,5*level))
    print('Press any key to continue.')