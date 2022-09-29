n,m = map(int,input().split())
check = [False]*(n+1)

def DFS(s,seq):
    if len(seq) == m:
        for s in seq:
            print(s,end = ' ')
        print()
        return 
    for i in range(s,n+1):
        if check[i] == False:
            seq.append(i)
            check[i] = True
            DFS(i+1,seq)
            check[i] = False
            seq.pop()

DFS(1,[])