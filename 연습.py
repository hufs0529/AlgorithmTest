n = int(input())
s = list(map(int, input().split()))
s = set(s)
a = list(s)
a.sort()
numdict = {}

for i in range(len(a)):
  numdict[a[i]] = i
  #
for i in s:
  print(numdict[i], end=' ')