n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] + arr[i]
cnt = 0

for i in range(n):
    for j in range(i+1, n+1):
        tmp = dp[j] - dp[i]
        if tmp == k:
            cnt += 1

print(cnt)