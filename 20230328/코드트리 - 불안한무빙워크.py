import sys
sys.stdin = open('input.txt','rt')

N,K = map(int,input().split())
save = list(map(lambda x: [int(x),0],input().split()))

# [0,1,N-1,...,2*N-1]
# 한 칸에 한 사람만, 사람 없으면 0 있으면 1

def walk_down():
    '''
    N번째 칸에 사람이 있는 경우 내리는 함수
    '''
    if save[N-1][1] == 1: 
        save[N-1][1] = 0

def rotate():
    '''
    무빙워크 회전
    '''
    global save
    save = [save[-1]] + save[:-1]
    walk_down()

def walk():
    '''
    사람 한 칸씩 이동
    가장 먼저 올라간 사람부터 -> N-1번부터 이동하기
    '''
    global cnt

    for i in range(N-2,-1,-1):
        if save[i][1] == 0: #현재 칸에 사람이 없는 경우
            continue
        if save[i+1][0] == 0 or save[i+1][1] == 1: #앞 칸 안정성이 0이거나 사람이 있거나?
            continue
        else:
            a,_ = save[i+1]
            save[i+1] = [a-1,1]     
            if save[i+1][0] == 0:
                cnt += 1 
            save[i][1] = 0 #다시 빈칸 처리

    walk_down()

def add_person():
    '''
    1번 칸에 사람 추가
    '''
    global cnt

    a,b = save[0]
    if b == 0 and a > 0:
        save[0] = [a-1,1]
        if save[0][0] == 0:
            cnt += 1

def debug():
    print(save)

cnt = 0

def simulate():
    t = 0
    while True:
        rotate()
        walk()
        add_person()
        t += 1
        if cnt >= K:
            print(t)
            break

simulate()