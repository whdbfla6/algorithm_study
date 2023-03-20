R,C = map(int,input().split())
dx,dy = [1,0,-1,0],[0,-1,0,1] #아래,왼,위,우
dic = {'|':{0,2},'-':{1,3},'1':{0,3},'2':{2,3},'3':{1,2},'4':{0,1},'+':{0,1,2,3}}
dic_rev = {tuple(v):k for k,v in dic.items()}

arr = [list(input()) for _ in range(R)]
blank = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'M': 
            sx,sy = i,j
        if arr[i][j] == 'Z': 
            ex,ey = i,j
        if arr[i][j] == '.': blank.append((i,j))

def find_blank(x,y):
    dir = []

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=R or ny<0 or ny>=C or arr[nx][ny] in ['.','M','Z']:
            continue
        s = arr[nx][ny]
        if i == 0:
            if 2 in dic[s]: dir.append(0)
        elif i == 1:
            if 3 in dic[s]: dir.append(1)
        elif i == 2:
            if 0 in dic[s]: dir.append(2)
        else:
            if 1 in dic[s]: dir.append(3)

    return dir

for x,y in blank:
    dir = find_blank(x,y)
    if len(dir)>0:
        dir = sorted(dir)
        print(x+1,y+1,dic_rev[tuple(dir)])
        break