pos_val_dic = {(0,x):y for x,y in enumerate(range(2,42,2),start=1)} #좌표 생성
pos_val_dic[(0,0)] = 0 #시작점
pos_val_dic[(0,21)] = 0 #끝점

val = [13,16,19,22,24,28,27,26,25,30,35]

for x in range(len(val)):
    pos_val_dic[(1,x)] = val[x] #좌표:해당하는 값

route = [[(0,x) for x in range(22)]] #4가지 길 생성

tmp = [(1,8),(1,9),(1,10),(0,20),(0,21)] # 25 30 35 40
route.append([(0,5),(1,0),(1,1),(1,2)] + tmp) # 10부터
route.append([(0,10),(1,3),(1,4)]+tmp) # 20부터
route.append([(0,15),(1,5),(1,6),(1,7)]+tmp) # 30부터

dice = list(map(int,input().split()))

def route_check(x,y):
    if x == 0 and y == 5: #(0, 5):10
        return 1
    elif x == 0 and y == 10: #(0, 10): 20
        return 2
    elif x == 0 and y == 15: #(0, 15): 30
        return 3
    else:
        return 0

answer = 0
position = [(0,0)]*4
visited = {key:False for key in pos_val_dic}

def DFS(depth,summ): #pos (그 길에서 몇번째 칸에 있는지, 어떤 길인지)
    
    global answer
    
    if depth == 10:
        answer = max(summ,answer)
        return
    
    num = dice[depth] 
    end = 0
    
    for i,val in enumerate(position):
        ind,r = val #그 길에서 몇번째 칸에 있는지, 어떤 길인지?
        if ind == len(route[r]) - 1: #이미 도착한 말
            end += 1
            continue
        x,y = route[r][ind]
        if ind+num >= len(route[r])-1: #도착
            ind = len(route[r])-1 #끝점으로 이동하기
            nx,ny = route[r][ind]
        else: 
            ind = ind + num #다음에 위치할 장소
            nx,ny = route[r][ind] 
            if r == 0: 
                r = route_check(nx,ny) #10,20,30 도달
                if r > 0: ind = 0 #새로운 루트의 0번째 인덱스로
        
        if not visited[(nx,ny)] or ind == len(route[r])-1:
            visited[(x,y)] = False #이전 위치 false
            visited[(nx,ny)] = True #다음 위치 true
            position[i] = (ind,r) #r번째 루트 ind번째
            
            DFS(depth+1,summ+pos_val_dic[(nx,ny)])
            
            visited[(x,y)] = True #back track
            visited[(nx,ny)] = False
            position[i] = val

    if end == 4: #말이 모두 도착지에 와있음
        answer = max(answer,summ)
        return

DFS(0,0)
print(answer)