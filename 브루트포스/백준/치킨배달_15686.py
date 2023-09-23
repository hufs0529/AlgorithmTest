from itertools import combinations

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
result = 1e9
houses, chickens = [], []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            houses.append([i, j])
        elif maps[i][j] == 2:
            chickens.append([i, j])

for comb in combinations(chickens, m):
    temp = 0
    for h in houses:
        chicken_len = 999
        for j in range(m):
            chicken_len = min(chicken_len, abs(h[0] - comb[j][0]) + abs(h[1] - comb[j][1]))
        temp += chicken_len
    result = min(result, temp)

print(result)
