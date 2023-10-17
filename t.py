n = int(input())
line = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)
print(result)