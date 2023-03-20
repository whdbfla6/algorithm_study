class Dlist:
    
    class Node:
        def __init__(self,prev,next,val):
            self.prev = prev
            self.next = next
            self.val = val

    def __init__(self):

        self.head = self.Node(prev=None,next=None,val=None)
        self.tail = self.Node(prev=None,next=None,val=None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = self.head

    def move_left(self):

        if self.cur == self.head:
            return
        self.cur = self.cur.prev

    def move_right(self):
        
        if self.cur.next == self.tail:
            return
        
        self.cur = self.cur.next

    def delete(self):
        if self.cur == self.head:
            return
        
        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev

        self.cur = self.cur.prev
    

    def insert(self,value):
        node = self.Node(prev=self.cur,next=self.cur.next,val=value)

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


