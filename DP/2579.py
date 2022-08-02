from sys import stdin
def dp(n):
    if n < 2:
        return
    dp(n-1)
    memory[n] = max(stair[n] + memory[n-2], stair[n] + stair[n-1] + memory[n-3])

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    num = int(stdin.readline())
    stair = [int(stdin.readline()) for _ in range(num)]

    memory = [0]*(num)
    memory[0] = stair[0]
    if num == 1: 
        print(memory[0])
    if num >= 2:
        memory[1] = stair[1] + stair[0]
        if num == 2: print(memory[1])
        else:
            dp(num-1)
            print(memory[-1])
