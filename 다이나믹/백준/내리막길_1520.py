dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
m, n = map(int, input().split())
maps = []
dp = [[-1] * n for _ in range(m)]
for _ in range(m):
    maps.append(list(map(int, input().split())))

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and maps[x][y] > maps[nx][ny]:
            ways += dfs(nx, ny)
    
    dp[x][y] = ways
    
    return dp[x][y]

print(dfs(0, 0))