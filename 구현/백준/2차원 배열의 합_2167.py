n, m = map(int, input().split())
s = []
dp = [[0] * (m+1) for _ in range(n+1)]
for _ in range(n):
  s.append(list(map(int, input().split())))
for i in range(m+1):
  for j in range(n+1):
    dp[i][j] = s[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
k = int(input())
for _ in range(k):
  i,j,x,y = map(int, input().split())
  print(dp[x][y] - dp[x][i-1] - dp[i-1][y] + dp[i-1][j-1])