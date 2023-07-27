r, c, q = map(int, input().split())
s = []
dp = [[0 for _ in range(c+1)] for _ in range(r+1)]

for _ in range(r):
    s.append(list(map(int, input().split())))

for i in range(1, r+1):
    for j in range(1, c+1):
        dp[i][j] = s[i-1][j-1] - dp[i-1][j-1] + dp[i][j-1] + dp[i-1][j]

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    num = ((x2-x1)+1) * ((y2-y1)+1)
    print(ans // num)
