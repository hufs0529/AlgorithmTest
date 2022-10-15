n = int(input())
k = int(input())
s = list(map(int, input().split()))
s.sort()
dist = []

for i in range(1, n):
  dist.append(abs(s[i] - s[i-1]))
dist.sort(reverse=True)

for _ in range(k-1):
  dist.pop(0)

print(sum(dist))