arr = [[-1,  0, 2, 0],
    [0, 10, 7, 1],
    [5,  2, 0, 1],
    [0, 8, 7, 1],
    [0,  0, 2, 0]]


N,M = 5,4
arr_ = [[0]*N for _ in range(M)]

for x in range(N):
    for y in range(M):
        arr_[M-1-y][x] = arr[x][y]


anti_clock = list(map(list,zip(*arr)))[::-1]

print(anti_clock)
print(arr_)

for x in range(N):
    for y in range(M):
        arr_[y][N-1-x] = arr[x][y]

clock = list(map(list,zip(*arr[::-1])))
print(clock)
print(arr_)