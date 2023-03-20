N,L = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

def check(tmp):
    global cnt

    point,flag = [],True
    for i in range(N-1):
        diff = tmp[i+1]-tmp[i]
        if diff == 0:
            continue
        elif diff == 1: #오르막
            point.append((i,-1)) #낮은지점, 왼쪽
        elif diff == -1: #내리막
            point.append((i+1,1)) #낮은지점, 오른쪽
        else:
            flag = False
    if flag:
        visited = [False]*N
        for p,diff in point:
            if not flag: break
            h = tmp[p]
            if diff == -1: r = range(p-L+1,p+1)
            else: r= range(p,p+L)
            for i in r:
                if i<0 or i>=N or visited[i] or h!=tmp[i]:
                    flag = False
                    break 
                visited[i] = True
    if flag: cnt += 1

for i in range(N):
    check(arr[i])
    check([arr[j][i] for j in range(N)])
print(cnt)