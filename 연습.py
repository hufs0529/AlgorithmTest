from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def bfs(xx, yy):
    each_cnt = 1
    queue = deque()
    queue.append((xx, yy))
    visited[xx][yy] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    each_cnt += 1
    return each_cnt

cnt, max_each_count = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_each_count = max(max_each_count, bfs(i,j))
            
print(cnt)
print(max_each_count)