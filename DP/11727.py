def solution(n):

    memory = [0]*1001
    memory[0] = 1 
    memory[1] = 3

    for i in range(2,n):
        memory[i] = memory[i-1] + memory[i-2] * 2
                
    return memory[n-1]


if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    print(solution(n))
    