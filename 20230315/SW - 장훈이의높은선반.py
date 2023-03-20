
def permutation(s,summ):
    global answer
    if summ >= B:
        answer = min(summ-B,answer)
        return
    
    for i in range(s,N):
        if not visited[i]:
            visited[i] = True
            permutation(i,summ+arr[i])
            visited[i] = False

T = int(input())

for t in range(1,T+1):
    N,B = map(int,input().split())
    arr = list(map(int,input().split()))
    answer = sum(arr)
    visited = [False]*N
    permutation(0,0)
    print('#{} {}'.format(t,answer))