n = int(input())
graph = list(map(int,input().split()))
delnode = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n):
    if graph[i] == -1: 
        tree[n].append(i) 
    else:
        tree[graph[i]].append(i)

answer = 0

def DFS(x):
    global answer
    if len(tree[x]) == 0:
        answer += 1
        return
    for i in range(len(tree[x])):
        if tree[x][i] == delnode:
            if len(tree[x]) == 1: #leaf가 한 개인데 삭제노드인 경우 카운트를 따로 해주어야 한다
                answer += 1
                return
            continue
        else:
            DFS(tree[x][i])

if graph[delnode] == -1:
    print(0)
else:
    DFS(n)
    print(answer)