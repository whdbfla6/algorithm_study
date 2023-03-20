class Dlist:
    
    class Node:
        def __init__(self,prev,next,val):
            self.prev = prev
            self.next = next
            self.val = val

    def __init__(self):
        

        self.head = self.Node(prev=None,next=None,val=None)
        self.tail = self.Node(prev=None,next=None,val=None)
        # HEAD와 TAIL을 연결해준다
        self.head.next = self.tail
        self.tail.prev = self.head

        # 커서를 기준으로 앞에 head가 있음을 의미
        # HEAD=CUR | TAIL
        self.cur = self.head 

    def move_left(self):

        # 맨 앞에 있는 상황으로 이동을 중단 PREV HEAD(CUR) | NODE
        if self.cur == self.head:
            return 
        # 앞으로 한 칸 이동 PREV CUR | NEXT -> PREV | CUR NEXT
        self.cur = self.cur.prev

    def move_right(self):
        
        # 뒤에 값이 tail인 경우 PREV CUR | TAIL(NEXT)인 상황 -> 이동 중단
        if self.cur.next == self.tail:
            return
        # 뒤로 한 칸 이동 PREV CUR | NEXT -> PREV NODE NEXT |
        self.cur = self.cur.next

    def delete(self):
        # 맨 앞에 있는 상황으로 지울 수 없음 HEAD(CUR) | NODE
        if self.cur == self.head:
            return
        
        # 현재 NODE를 기준으로 앞뒤에 있는 NODE를 서로 연결해줌
        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev

        # 현재 노드를 앞에 있는 노드로 업데이트
        # PREV NODE | NEXT -> PREV | NEXT
        self.cur = self.cur.prev
    

    def insert(self,value):
        node = self.Node(prev=self.cur,next=self.cur.next,val=value)

        # PREV CUR | NEXT -> PREV CUR NODE | NEXT 
        self.cur.next.prev = node
        self.cur.next = node

        self.cur = node


N = int(input())
for _ in range(N):    
    order = list(input())
    dlist = Dlist()

    for o in order:
        if o == '<':
            dlist.move_left()
        elif o == '>':
            dlist.move_right()
        elif o == '-':
            dlist.delete()
        else:
            dlist.insert(o)

    node = dlist.head.next
    while True:
        if node == dlist.tail:
            break
        print(node.val,end='')
        node = node.next
    print()


