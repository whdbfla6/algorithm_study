
stdin = open("../input.txt",'rt')
n,k = map(int,stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
memory = [1000000]*(max(n,k)+1)


for coin in coins:
    memory[coin] = 1

for coin in coins:
    for i in range(1,k+1):
        if i>coin:
            memory[i] = min(memory[i-coin]+1,memory[i])


if memory[k] == 1000000:
    print(-1)
    exit()

print(memory[k])