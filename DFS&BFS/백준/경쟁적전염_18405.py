dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
from collections import deque

n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
s, x, y = map(int, input().split())

def bfs(s, x, y):
    queue = deque(virus)
    count = 0
    while queue:
        if count == s:
            break
        for _ in range(len(queue)):
            prev, x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        queue.append((graph[nx][ny], nx, ny))
        count += 1
    return graph[x-1][y-1]

virus.sort()
print(bfs(s, x, y))
