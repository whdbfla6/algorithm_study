
stdin = open("../input.txt",'rt')
n,k = map(int,stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
memory = [10000]*(k+1)
memory[0] = 1

for i in range(1,k+1):
    for coin in coins:
        if i>=coin:
            memory[i] = min(memory[i],memory[i-coin]+1)

print(memory[-1])