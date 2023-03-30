import sys
sys.stdin = open('input.txt','rt')


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

dx,dy = [0,1,0,-1],[-1,0,1,0] #왼,아래,오,위
dir = {0:{(-2,0):2,(-1,-1):10,(-1,0):7,(-1,1):1,(0,-2):5,(1,-1):10,(1,0):7,(1,1):1,(2,0):2,(0,-1):0}}

for i in range(1,4):
    dir[i] = {}
    for x,y in dir[i-1]:
        dir[i][(-y,x)] = dir[i-1][(x,y)]


def clean(x,y,d):
    '''
    방향이 주어지면 비율에 따라 청소하는 함수
    [input] 방향
    '''
    global answer
    dust = arr[x][y] #원래 먼지 양 기억해주기
    
    for i,j in dir[d]:

        nx = x+i
        ny = y+j

        moved_dust = dust * dir[d][(i,j)] // 100
        if dir[d][(i,j)] == 0: 
            moved_dust = arr[x][y]

        arr[x][y] -= moved_dust

        if nx<0 or nx>=N or ny<0 or ny>=N:
            answer += moved_dust
            continue

        arr[nx][ny] += moved_dust
    

def clean_all():
    cnt,d = 1,0
    x,y = N//2, N//2
    flag = True

    while flag:
        for _ in range(2):
            if not flag: 
                break
            for _ in range(cnt):
                x,y = x+dx[d],y+dy[d]
                clean(x,y,d)
                if x == 0 and y == 0:
                    flag = False
                    break
            d = (d+1) % 4 # 시계방향
        cnt += 1

answer = 0
clean_all()
print(answer)

