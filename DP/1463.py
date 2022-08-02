from sys import stdin
# from time import time

def solution(n):
    for i in range(2,n+1):
        memory[i] = memory[i-1] + 1
        if i%2 == 0:
            memory[i] = min(memory[i],memory[i//2]+1)
        if i%3 == 0:
            memory[i] = min(memory[i],memory[i//3]+1)

answer = 10

def solution_dfs(n,cnt):
    global answer
    if n == 1:
        if cnt < answer: answer = cnt
        return 
    if n < 1:
        return 
    if n%2 == 0:
        solution_dfs(n//2,cnt+1)
    if n%3 == 0:
        solution_dfs(n//3,cnt+1)
    solution_dfs(n-1,cnt+1)
        
    

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    memory = [0]*(n+1)
    solution(n)
    print(memory[n])
    