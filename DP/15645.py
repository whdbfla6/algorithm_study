n = int(input())

board_max = list(map(int,input().split()))
board_min = list(board_max)

for _ in range(n-1):
    a,b,c = map(int,input().split())
    for y in range(3):
        if y == 0:
            board_min[y] = board_min[y] + min(a,b)
            board_max[y] = board_max[y] + max(a,b)
        if y == 1:
            board_min[y] = board_min[y] + min(a,b,c)
            board_max[y] = board_max[y] + max(a,b,c)
        if y == 2:
            board_min[y] = board_min[y] + min(b,c)
            board_max[y] = board_max[y] + max(b,c)

print(max(board_max),min(board_min))