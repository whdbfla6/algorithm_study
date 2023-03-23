
import sys
sys.stdin = open('20230323/input.txt','rt')


pos_val_dic = {(0,x):y for x,y in enumerate(range(2,42,2),start=1)} #좌표 생성
pos_val_dic[(0,0)] = -1
val = [13,16,19,22,24,28,27,26,25,30,35]
for x in range(len(val)):
    pos_val_dic[(1,x)] = val[x] #좌표:해당하는 값

route = [[(0,x) for x in range(20)]] #4가지 길 생성
tmp = [(1,8),(1,9),(1,10),(0,19)]
route.append([(0,5),(1,0),(1,1),(1,2)] + tmp)
route.append([(0,10),(1,3),(1,4)]+tmp)
route.append([(0,15),(1,5),(1,6),(1,7)]+tmp)

dice = list(map(int,input().split()))

def route_check(x,y):
    if x == 0 and y == 4: #(0, 4):10
        return 1
    elif x == 0 and y == 9: #(0, 9): 20
        return 2
    elif x == 0 and y == 14: #(0, 14): 30
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
    
    num = dice[depth] #두칸이동 = 4 = (0,1)
    
    end = 0
    for i,val in enumerate(pos):
        ind,r = val #그 길에서 몇번째 칸에 있는지, 어떤 길인지?
        if r == -1: #말이 종료
            end += 1
            continue
        if ind+num > len(route[r]): #이동하니 도착함
            pos[i] = (0,-1)
            # visited
            DFS(depth+1,cnt,pos,visited,summ)
            pos[i] = val
        # else:
        #     nx,ny = route[r][ind+num] #이동한 위치
        #     newr = route_check(r) # 새로운 길
        #     if newr == 0:
        #         pos[i] = (ind+num,newr)
        #     else:
        #         pos[i] = (0,newr)
        #     DFS(depth+1,cnt,pos,summ+pos_val_dic[(nx,ny)])
        #     pos[i] = val #복구
    
    if end == 4: #모든 말이 도착함
        answer = max(answer,summ)
        return


# DFS(0,4,[],0)
# print(answer)
