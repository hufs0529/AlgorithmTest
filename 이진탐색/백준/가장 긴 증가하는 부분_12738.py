from bisect import bisect_left

n = int(input())
s = list(map(int, input().split()))
dp = []

for num in s:
    k = bisect_left(dp, num)
    if k == len(dp):
        dp.append(num)
    else:
        dp[k] = num

print(len(dp))