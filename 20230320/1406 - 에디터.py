class Text:
    def __init__(self,value=None,cur=None,pre=None,next=None):
        self.value = value
        self.cur = cur
        self.pre = pre
        self.next = next

st = list(input())
N = len(st)
cursers = [Text(value=-1,next=1,cur=0)]
for i in range(N-1):
    cursers.append(Text(value=st[i],pre=i,cur=i+1,next=i+2))
cursers.append(Text(value=st[-1],cur=N,pre=N-1,next=-1))

k = N
M = int(input())

for _ in range(M):
    order = input()
    c = cursers[k]
    if order == 'L': #왼쪽
        if c.value != -1:
            k = c.pre
    elif order == 'D': #오른쪽
        if c.next != -1:
            k = c.next
    elif order == 'B':
        if c.value == -1:
            continue
        cursers[c.pre].next = c.next
        if c.next != -1:
            cursers[c.next].pre = c.pre
        k = c.pre
        c = cursers[k]
    else:
        X = order.split()[1]
        N += 1
        newc = Text(value=X,cur=N)
        newc.pre = c.cur
        newc.next = c.next
        cursers.append(newc)

        if c.next != -1:
            cursers[c.next].pre = N
        cursers[k].next = N
        k = N

answer = ''
k = cursers[0].next

while True:
    c = cursers[k]
    print(c.value,end="")
    k = c.next
    if k == -1:
        break