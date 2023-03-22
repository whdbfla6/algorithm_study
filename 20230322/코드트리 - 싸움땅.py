# import sys
# sys.stdin = open('input.txt','rt')
import heapq
dx,dy = [-1,0,1,0],[0,1,0,-1]

N,M,K = map(int,input().split())
arr = [[[[],0] for _ in range(N)] for _ in range(N)] #[[총],[사람]]

for i in range(N): 
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j]>0: 
            heapq.heappush(arr[i][j][0],-tmp[j])

info = {} # playernun = (d,s,w) 방향 초기 소유한 총

for i in range(1,M+1):
    x,y,d,s = map(int,input().split())
    arr[x-1][y-1][-1] = i
    info[i] = [x-1,y-1,d,s,0]

def flip(d):
    if d == 0 or d == 1:
        return d+2
    else:
        return d-2

point = [0]*M

def get_gun(x,y,w): #좌표, 기존무기
    global arr
    tmp = -heapq.heappop(arr[x][y][0])  # 놓여있는 총 중에서 공격력이 가장 강한 총
    if tmp > w: #가장 공격력이 높은 총을 획득
        if w > 0: heapq.heappush(arr[x][y][0],-w) #기존 총 버림, 총이 있었던 경우만
        w = tmp
    else:
        heapq.heappush(arr[x][y][0],-tmp) # 다시 넣어준다
    return w 

def position_update(nx,ny,k):
    arr[nx][ny][-1] = k
    info[k][:2] = [nx,ny] 

def move(k): #k번째 사람 이동
    x,y,d,s,w = info[k]
    nx,ny = x+dx[d],y+dy[d] #이동
    
    if nx<0 or nx>=N or ny<0 or ny>=N:
        d = flip(d)
        nx,ny = x+dx[d],y+dy[d]
        info[k][2] = d

    arr[x][y][1] = 0
    
    if arr[nx][ny][1] == 0: # 플레이어가 없는 경우
        if len(arr[nx][ny][0])>0:
            info[k][-1] = get_gun(nx,ny,w) # 새로 업데이트된 무기 공격력
        position_update(nx,ny,k)
    
    else:
        player = arr[nx][ny][1]
        tmp = info[player] #기존 플레이어의 정보
        power = tmp[-2] + tmp[-1] #힘
        
        if power > s+w or (power == s+w and tmp[-2] > s):
            win,loose = player,k
        else:
            win,loose = k,player

        position_update(nx,ny,win) #이긴사람의 위치 업데이트
        point[win-1] += abs(power-s-w) #각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트

        if info[loose][-1] > 0: # 2-2-2 본인이 가지고 있는 총을 해당 격자에 내려놓기
            heapq.heappush(arr[nx][ny][0],-info[loose][-1])
            info[loose][-1] = 0
        
        # 2-2-2 진 사람 이동
        ld = info[loose][2]
        x,y = nx,ny #결투한 위치

        for _ in range(4):
            nx,ny = x+dx[ld],y+dy[ld]
            if nx<0 or nx>=N or ny<0 or ny>=N or arr[nx][ny][-1]>0:
                ld = (ld+1)%4
            else:
                info[loose][2] = ld #방향 수정
                if len(arr[nx][ny][0]) > 0: #이동 후에 무기 변경
                    info[loose][-1] = get_gun(nx,ny,info[loose][-1])

                # 진 사람 위치 없데이트
                position_update(nx,ny,loose)
                break

        if len(arr[x][y][0])>0: #이긴사람 무기 변경
            info[win][-1] = get_gun(x,y,info[win][-1])

for _ in range(K):
    for m in range(1,M+1):
        move(m)

print(' '.join(map(str,point)))
