def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

from collections import deque

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)