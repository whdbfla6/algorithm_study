import sys
sys.stdin = open('input.txt','rt')

class People:
    class Node:
        def __init__(self,num,prev,next):
            self.num = num
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = self.Node(None,None,None)
        self.cur = self.head
        
        self.cnt = 0
        self.nodeinfo = {}

    def insert(self,num):
        node = self.Node(num = num, prev = self.cur, next = self.head)
        node.prev.next = node
        node.next.prev = node

        self.nodeinfo[num] = node
        self.cnt += 1
        self.cur = node

    def delete(self,num):
        node = self.nodeinfo[num]
        a,b = node.prev, node.next
        node.prev.next = b
        node.next.prev = a

        self.cnt -= 1

def debug():
    cur = people.head.next
    while True:
        if cur == people.head:
            break
        print(cur.num)
        cur = cur.next
    print()
    cur = people.head.prev
    while True:
        if cur == people.head:
            break
        print(cur.num)
        cur = cur.prev

# people.insert(1)
# people.insert(2)
# debug()

people = People()
N,K = map(int,input().split())
for i in range(1,N+1):
    people.insert(i)

cur = people.head
nums = []

while people.cnt > 0:
    for _ in range(K):
        cur = cur.next
        if cur == people.head: 
            cur = people.head.next
    people.delete(cur.num)
    nums.append(cur.num)

answer = '<'
for i in nums[:-1]:
    answer += str(i) +', '
answer += str(nums[-1]) + '>'

print(answer)



