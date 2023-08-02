n, m = map(int, input().split())
s = []
dp = [[0]* (n+1) for _ in range(n+1)]

for _ in range(n):
    s.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    for j in range(1, n+1):  # The loop should run up to 'n+1'
        dp[i][j] = s[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]  

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(res)