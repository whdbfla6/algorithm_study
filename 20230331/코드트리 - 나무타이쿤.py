import sys
sys.stdin = open('input.txt','rt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
info = [tuple(map(int,input().split())) for _ in range(M)]
info.insert(0,[])

dx,dy = [0,0,-1,-1,-1,0,1,1,1],[0,1,1,0,-1,-1,-1,0,1]
pos = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]

def debug():
    print(pos)
    for a in arr:
        print(a)
    print()

def move(level):
    '''
    [인풋] 영양제 위치 리스트
    끝이 0이랑 이어져 있음 -> 나머지로 구현
    영양제 개수만큼 돌면서 좌표 바꿔주기
    '''
    global pos
    d,p = info[level]

    for i in range(len(pos)):
        x,y = pos[i]
        nx,ny = x+dx[d]*p, y+dy[d]*p
        pos[i] = (nx%N,ny%N)

import copy
def input():
    '''
    해당 땅에 특수영양제 투입
    1씩 증가하면 된다
    대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장
    '''
    global arr

    for x,y in pos:
        arr[x][y] += 1

    arr_ = copy.deepcopy(arr)

    for x,y in pos:
        cnt = 0 #대각선 방향 리브로수 개수
        for i in range(2,9,2):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]>=1:
                cnt += 1
        arr_[x][y] += cnt

    arr = arr_


def remove():
    '''
    특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는 
    높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고
    영양제 위치, CNT 다시 넣어주기
    '''
    global pos

    newpos = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i,j) not in pos:
                arr[i][j] -= 2
                newpos.append((i,j))
    pos = newpos


def solution(level):
    move(level)
    input()
    remove()

for i in range(1,M+1):
    solution(i)

answer = 0
for x in range(N):
    for y in range(N):
        answer += arr[x][y]
print(answer)



