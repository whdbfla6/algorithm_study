# alph = [chr(i) for i in range(97,123)]
# print(alph)

L,C = map(int,input().split())
chrs = list(map(str,input().split()))
chrs = sorted(chrs)

def DFS(st):
    if len(st) == L:
        v,c = 0,0
        for i in st:
            if i in ['a','e','o','u','i']:
                v += 1
            else:
                c += 1
        if v >= 1 and c>=2:
            for i in st:
                print(i,end='')
            print()
        return
    for i in chrs:
        if len(st) == 0 : 
            st.append(i)
            DFS(st)
            st.pop()
        elif ord(i) > ord(st[-1]): 
            st.append(i)
            DFS(st)
            st.pop()


DFS([])


