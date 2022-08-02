[시간복잡도](#시간복잡도)

[순열,조합](#순열-조합)

[찾기(리스트,상하좌우)](#찾기)

## 시간복잡도

|데이터 수|시간복잡도|대표알고리즘|
|------|-----|------|
|500|O(N^3)|-|
|2000|O(N^2)|-|
|100000|O(NlogN)|이진탐색|
|10000000|O(N)|-|

```{bash}
.
├── readme.md
└── 리스트.ipynb
```

## 순열 조합

### 순열

```{python}
n = 3 ; r = 2
check = [0]*(n+1)
answer = [0] * r

def DFS(L):
    global n,r
    if L == r:
        print(tuple(answer),end=' ')
        return
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                answer[L] = i
                check[i] = 1
                DFS(L+1)
                check[i] = 0 #i=2인 경우 다시 1을 읽어야하기 때문에 check[1]=0으로 복구
DFS(0)

```
```
from itertools import permutations

list(permutations(range(1,4),2))
```

### 조합

```{python}
n = 4 ; r = 2 
answer = [0] * r


def DFS(L,begin):
    global n,r
    if L == r:
        print(tuple(answer),end=' ')
        return
    else:
        # 본인보다 큰 숫자에 대해서 for문이 반복되기 때문에 check할 필요 없음
        for i in range(begin,n+1):
            answer[L] = i
            DFS(L+1,i+1)
DFS(0,1)
```

```{python}
from itertools import combinations

list(combinations(range(1,5),2))
```

### 찾기

```{python}
N,M = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))
```
```{python}
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def search(x,y):
    for i in range(4):
        nx = x + dx[i] ; ny = y + dy[i]
        if nx>=0 and nx<N and ny >=0 and ny<M:
            search(nx,ny)
```

## 관련링크

[프로그래밍 팀 노트](https://github.com/ndb796/Python-Competitive-Programming-Team-Notes)