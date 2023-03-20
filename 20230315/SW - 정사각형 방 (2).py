def dfs(r, c, diff):
    global cnt, max_cnt, room_num
 
    cnt += 1
    visit[r][c] = True
    if cnt > max_cnt:
        max_cnt = cnt
        room_num = A[r][c]
 
    if cnt == max_cnt:
        if room_num > A[r][c]:
            room_num = A[r][c]
 
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if A[nr][nc] == A[r][c] + diff:
                dfs(nr, nc, diff)
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [[*map(int, input().split())] for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    drc = ((-1, 0), (1, 0), (0, -1), (0, 1))
    max_cnt = 0
    room_num = 1e9
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                cnt = 0
                dfs(i, j, 1)
                dfs(i, j, -1)
 
    print(f'#{tc} {room_num} {max_cnt - 1}')
