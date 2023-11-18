n = int(input())
grid = []
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for _ in range(n):
    grid.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if grid[i][j] != 0 and dp[i][j] != 0:
            if i + grid[i][j] < n:
                dp[i+grid[i][j]][j] += dp[i][j]
            if j + grid[i][j] < n:
                dp[i][j+grid[i][j]] += dp[i][j]

print(dp[-1][-1])