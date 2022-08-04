
stdin = open("../input.txt",'rt')
n = int(stdin.readline())
stone = [list(map(int,stdin.readline().split())) for _ in range(n-1)]
k = int(stdin.readline())

memory =  [0] * n

memory[0] = 0
if n == 1:
    print(memory[-1])
    exit()
memory[1] = stone[0][0]
if n == 2:
    print(memory[-1])
    exit()
memory[2] = min(stone[0][1],stone[0][0]+stone[1][0])
if n == 3:
    print(memory[-1])
    exit()    
min_val = 1000000000
min_val = 1000000

for j in range(3,n):
    for i in range(3,n):
        memory[i] = min(memory[i-1]+stone[i-1][0],memory[i-2]+stone[i-2][1])
        if i == j:
            memory[i] = min(memory[i-3] + k, memory[i])
    if memory[-1] < min_val:
        min_val = memory[-1]

print(min_val)