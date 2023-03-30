
score = [0,1,10,100,1000]
N = int(input())
arr = [[0]*N for _ in range(N)]
like_info = {}

'''
1번 조건에서 네 방향을 돌면서 좋아하는 친구인지 아닌지 접근해야 하기 때문에
set으로 설정해두자
'''
for _ in range(N**2):
    tmp = list(map(int,input().split()))
    like_info[tmp[0]] = set(tmp[1:])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def get_position(num):
    '''
    1번 2번 조건에 만족하는 좌표들을 반환하는 함수
    (좋아하는친구수,인접한칸의 수, 행, 열)
    [input] 학생번호 [output] 가능한 좌표들
    '''
    ax = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] > 0 :
                continue

            friend, blank = 0,0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue

                if arr[nx][ny] in like_info[num]:
                    friend += 1
                elif arr[nx][ny] == 0:
                    blank += 1

            ax.append((friend,blank,x,y))
    
    ax = sorted(ax,key = lambda x:(-x[0],-x[1],x[2],x[3]))
    return ax[0][2], ax[0][3]


def set_students():
    '''
    학생 N**2명을 배치하는 함수
    '''
    for num in like_info:
        x,y = get_position(num)
        arr[x][y] = num


def get_score():

    answer = 0
    for x in range(N):
        for y in range(N):
            
            friend = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if arr[nx][ny] in like_info[arr[x][y]]:
                    friend += 1

            answer += score[friend]

    return answer

set_students()
print(get_score())
