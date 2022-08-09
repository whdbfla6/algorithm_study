# https://dailymapins.tistory.com/91

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]

check[0][0] = 1

for i in range(n):
    for j in range(n):
        if check[i][j] != 0:
            if board[i][j] == 0:
                print(check[n-1][n-1])
                exit()
            jump = board[i][j]
            if i + jump < n: check[i+jump][j] += check[i][j]
            if j + jump < n: check[i][j+jump] += check[i][j]