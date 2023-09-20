dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
cnt = 0

def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)
    return cnt

result = []
for i in range(m):
    for j in range(n):
        cnt = dfs(i, j)
        if cnt:
            result.append(cnt)
            
