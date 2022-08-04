from sys import stdin
def solution(n,arr):
    for i in range(1,n):
        arr[i][0] = min(arr[i-1][1],arr[i-1][2]) + arr[i][0]
        arr[i][1] = min(arr[i-1][2],arr[i-1][0]) + arr[i][1]
        arr[i][2] = min(arr[i-1][0],arr[i-1][1]) + arr[i][2]
    return min(arr[n-1])

if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    n = int(stdin.readline())
    arr = [list(map(int,stdin.readline().split())) for _ in range(n)]
    print(solution(n,arr))