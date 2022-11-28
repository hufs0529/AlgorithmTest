t = int(input())

for i in range(t):
  n = int(input())
  trees = list(map(int, input().split()))
  trees.sort()
  res = 0
  for j in range(2, n):
    res = max(res, abs(trees[j] - trees[j-2]))
  print(res)