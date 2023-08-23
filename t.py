from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)]for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += bfs(i, j)


def bfs(x, y):
    queue = deque([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 2
    return 1