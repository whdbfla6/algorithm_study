st = set('antatica')
N,K = map(int,input().split())
visited = [False]*(123-97)
for s in st:
    visited[ord(s)-97] = True
    K -= 1

res = set('antatica')
words = [set(input()) for _ in range(N)]
answer = 0

def DFS(s,depth):
    global answer
    if depth == K:
        cnt = 0
        for word in words:
            if len(word-res) == 0:
                cnt += 1
        answer = max(answer,cnt)
        return
    for i in range(s,123-97):
        if not visited[i]:
            visited[i] = True
            res.add(chr(i+97))
            DFS(i+1,depth+1)
            res.remove(chr(i+97))
            visited[i] = False

DFS(0,0)
print(answer)