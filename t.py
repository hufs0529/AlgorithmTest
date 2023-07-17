from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
                field[nx][ny] = 2
                queue.append([nx, ny])


t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                field[i][j] = 0
                bfs(i, j)
                cnt += 1
    print(cnt)
