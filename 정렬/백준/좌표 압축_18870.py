n = int(input())
s = list(map(int, input().split()))
numset = set(s)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
  numdict[a[i]] = i
  
for i in s:
  print(numdict[i], end=' ')