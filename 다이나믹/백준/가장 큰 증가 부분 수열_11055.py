n = int(input())
s = list(map(int, input().split()))

dp = [1] * n
dp[0] = s[0]

for i in range(1, n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[i], dp[j] + s[i])
        else:
            dp[i] = max(dp[i], s[i])
print(max(dp))