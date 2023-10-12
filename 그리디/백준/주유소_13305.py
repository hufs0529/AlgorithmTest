n = int(input())
road = list(map(int, input().split())) # 2 3 1
cost = list(map(int, input().split())) # 5 2 4 1
res = 0
m = cost[0] # 5

for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    res += m*road[i]