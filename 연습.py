D, K = map(int, input().split())

dp = [] * D

for i in range(1, K//2+1):
  for j in range(i+1, K):
    dp[0] = i
    dp[1] = j
    for k in range(2, D):
      dp[k] = dp[k-1] + dp[i-2]
      
    if dp[D-1] == K:
      print(dp[0])
      print(dp[1])
      