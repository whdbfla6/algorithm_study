from sys import stdin

def solution(n,snack):
    memory[0] = snack[0]
    memory[1] = max(snack[0],snack[1])
    for i in range(2,n):
        memory[i] = max(memory[i-2] + snack[i],memory[i-1])

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    memory = [0]*(n+1)
    snack = list(map(int,stdin.readline().split()))

    solution(n,snack)
    print(memory[n-1])