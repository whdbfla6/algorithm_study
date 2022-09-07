n,m = map(int,input().split())
check = [False]*(n+1)

def DFS(seq):
    if len(seq) == m:
        for s in seq:
            print(s,end = ' ')
        print()
        return 
    for i in range(1,n+1):
        if check[i] == False:
            seq.append(i)
            check[i] = True
            DFS(seq)
            check[i] = False
            seq.pop()

DFS([])