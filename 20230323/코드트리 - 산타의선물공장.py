class Belt:
    class Box:
        def __init__(self,id,weight,prev,next):
            self.id = id
            self.weight = weight
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Box(id=None,weight=None,prev=None,next=None)
        self.tail = self.Box(id=None,weight=None,prev=None,next=None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.status = True #작동됨
        self.id_dict = {} #객체 저장 id:Box

    def insert_head(self,id,weight):
        box = self.Box(id=id,weight=weight,prev=self.head,next=self.head.next)

        box.prev.next = box
        box.next.prev = box
        self.id_dict[id] = box

    def insert_tail(self,id,weight):
        box = self.Box(id=id,weight=weight,prev=self.tail.prev,next=self.tail)

        box.prev.next = box
        box.next.prev = box
        self.id_dict[id] = box

    def delete(self,id): #맨 뒤 제거: self.tail.prev.id, 맨 앞 제거: self.head.next.id
        box = self.id_dict[id]
        prev,next = box.prev,box.next

        prev.next = next
        next.prev = prev
        del self.id_dict[id]

def debug():
    for i in range(M):
        print(i+1,'번째 belt 디버깅')
        belt = belts[i]
        if not belt.status:
            print('벨트 고장')
            return
        print('head to tail')
        cur = belt.head.next
        while True: #head - tail
            if cur == belt.tail:
                break
            print(cur.id,cur.weight)
            cur = cur.next
        
        print('tail to head')
        cur = belt.tail.prev
        while True:
            if cur == belt.head:
                break
            print(cur.id,cur.weight)
            cur = cur.prev
            


q = int(input())
first_order = list(map(int,input().split()))[1:]
N,M = first_order[:2]
ids,ws = first_order[2:N+2],first_order[N+2:]

belts = [Belt() for _ in range(M)]
check = [True]*M
b = 0
for i in range(0,N,N//M):
    for id,weight in zip(ids[i:i+N//M],ws[i:i+N//M]):
        belts[b].insert_tail(id,weight)
    b += 1

def order_200(w_max):
    answer = 0
    for i in range(M):
        belt = belts[i]
        if not belt.status: #고장난 벨트는 작동 안 함
            continue

        box = belt.head.next #맨 앞 상자
        if box == belt.tail: # 상자가 하나도 없는 경우
            continue
        
        belt.delete(box.id)
        if box.weight <= w_max:
            answer += box.weight
        else:
            belt.insert_tail(box.id,box.weight)
    print(answer)


def order_300(r_id):
    for i in range(M):
        belt = belts[i]
        if not belt.status:
            continue

        if r_id in belt.id_dict:
            print(r_id)
            belt.delete(r_id)
            break
    else:
        print(-1)


def order_400(f_id):
    for i in range(M):
        belt = belts[i]
        if not belt.status:
            continue

        if f_id in belt.id_dict:
            print(i+1)
            belt.head.next.prev = belt.tail.prev
            belt.tail.prev.next = belt.head.next

            belt.id_dict[f_id].prev.next = belt.tail
            belt.tail.prev = belt.id_dict[f_id].prev

            belt.head.next = belt.id_dict[f_id]
            belt.id_dict[f_id].prev = belt.head
            break
    else:
        print(-1)


def move_all_box(prevbelt,nextbelt):

    nextbelt.tail.prev.next = prevbelt.head.next
    prevbelt.head.next.prev = nextbelt.tail.prev

    prevbelt.tail.prev.next = nextbelt.tail
    nextbelt.tail.prev = prevbelt.tail.prev

    nextbelt.id_dict.update(prevbelt.id_dict)


def order_500(b_num):
    if not belts[b_num].status: #이미 고장난 경우
        print(-1)
        return
    
    print(b_num+1)
    prevbelt = belts[b_num]
    status = False

    for i in range(b_num+1,M):
        nextbelt = belts[i]
        if not nextbelt.status: #벨트가 고장났는지 확인
            continue
        status = True
        move_all_box(prevbelt,nextbelt)
        break

    if not status: #정상 벨트를 못 찾은 경우
        for i in range(b_num):
            nextbelt = belts[i]
            if not nextbelt.status:
                continue
            move_all_box(prevbelt,nextbelt)
            break
    
    prevbelt.status = False #고장 처리



for _ in range(q-1): 
    order,num = map(int,input().split())
    if order == 200:
        order_200(num)
    elif order == 300:
        order_300(num)
    elif order == 400:
        order_400(num)
    else:
        order_500(num-1)