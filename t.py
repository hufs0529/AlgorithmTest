n = int(input())
k = map(int, input().split())
spot = list(map(int, input().split()))
spot.sort()
# 1 3 6 6 7 9

dist = []

for i in range(1, n):
    dist.append(abs(spot[i] - spot[i-1]))
dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)
print(sum(dist))