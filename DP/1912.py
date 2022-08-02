def solution(arr):
    for i in range(2,n):
        memory[i] = max(memory[i-1]+arr[i],arr[i])


if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))

    memory = [0]*n
    memory[0] = arr[0]
    memory[1] = max(arr[1],arr[1]+arr[0])
    solution(arr)
    print(max(memory))