def solution(arr):
    for i in range(1,n):
        for j in range(i):
            if arr[i] > arr[j]:
                memory[i] = max(memory[i],memory[j]+1)
                
    return max(memory)


if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))

    memory = [1]*(n+1)
    print(solution(arr))