n = int(input())
road = list(map(int, input().split())) # 2 3 1
cost = list(map(int, input().split())) # 5 2 4 1

dp = [0] * n
dp[0] = cost[0] * road[0]
m = 0

for i in range(1, n-1):
    m = min(m, cost[i])
    dp[i] = m * road[i]