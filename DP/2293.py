n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
memory = [0]*(k+1)
memory[0] = 1

for coin in coins:
    for i in range(1,k+1):
        if i>=coin:
            memory[i] += memory[i-coin]

print(memory[k])