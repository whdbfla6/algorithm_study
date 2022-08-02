def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2 # 2, 1+1
    if n == 3:
        return 4 # 2+2, 2+1+1, 1+2, 1+1+1
    return solution(n-1) + solution(n-2) + solution(n-3)



if __name__ == "__main__":
    stdin = open("../input.txt",'rt')
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        print(solution(n))