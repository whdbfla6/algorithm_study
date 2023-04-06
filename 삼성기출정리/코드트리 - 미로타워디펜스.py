'''
죽은 몬스터 -1만들어줘서 그 아이들만 사라지게 하자
'''
from collections import deque

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
info = [tuple(map(int,input().split())) for _ in range(M)]
info.insert(0,[])

dx,dy = [0,1,0,-1],[1,0,-1,0]
CENTER = N//2
POINT = 0

def attack_monster(level):
    '''
    몬스터 공격해서 제거
    '''
    global POINT
    x,y = CENTER,CENTER
    d,p = info[level]

    for _ in range(p):
        x,y = x+dx[d], y+dy[d]
        POINT += arr[x][y]
        arr[x][y] = -1

def make_one_dimension():
    '''
    중심에서 시작해서 1차원으로 만들어준다
    '''
    dx,dy = [0,1,0,-1],[-1,0,1,0]
    x,y = CENTER,CENTER
    flag, cnt, d = True, 1, 0

    res = deque([arr[x][y]])

    while flag:
        for _ in range(2):
            if not flag: break
            for _ in range(cnt):
                x = x+dx[d]
                y = y+dy[d]
                if arr[x][y] == 0:
                    flag = False
                    break
                res.append(arr[x][y])
                if x == 0 and y == 0:
                    flag = False
                    break
            d = (d+1) % 4
        cnt += 1

    return res


def remove_blank(res):
    '''
    -1인 아이들 pop시켜주는 함수
    '''
    newres = deque()
    while res:
        x = res.popleft()
        if x == -1:
            continue
        newres.append(x)
    
    return newres

def one_dimension_to_arr(res):
    '''
    1차원 다시 배열로 넣는 함수
    '''
    global arr

    dx,dy = [0,1,0,-1],[-1,0,1,0]
    x,y = CENTER,CENTER
    flag, cnt, d = True, 1, 0
    arr_ = [[0]*N for _ in range(N)]
    res.popleft()

    while flag:
        for _ in range(2):
            if not flag: break
            for _ in range(cnt):
                x = x+dx[d]
                y = y+dy[d]
                if not res:
                    flag = False
                    break
                arr_[x][y] = res.popleft()
                if x == 0 and y == 0:
                    flag = False
                    break
            d = (d+1) % 4
        cnt += 1

    arr = arr_

def remove_continuous_monster(res):
    '''
    4번 이상 등장하는 몬스터 죽이기
    '''
    global POINT,flag

    newres = deque()

    while res:
        pre = res.popleft()
        cnt = 1
        while res:
            cur = res.popleft()
            if cur != pre:
                res.appendleft(cur)
                break
            cnt += 1
        if cnt >= 4:
            POINT += cnt * pre
        else:
            newres.extend([pre]*cnt)

    return newres

def make_pair(res):

    newres = deque()
    newres.append(res.popleft()) # 가운데 탑

    while res:
        pre = res.popleft()
        cnt = 1
        while res:
            cur = res.popleft()
            if cur != pre:
                res.appendleft(cur)
                break
            cnt += 1
        newres.extend([cnt,pre])

    return newres

for i in range(1,M+1):

    attack_monster(i)
    res = make_one_dimension()
    res = remove_blank(res)

    flag = True
    while flag:
        flag = False
        res = remove_continuous_monster(res)

    res = make_pair(res)
    one_dimension_to_arr(res)
    break

print(POINT)