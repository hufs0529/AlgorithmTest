from itertools import combinations

n = int(input())
s = []

for i in range(1, 11):
  for comb in combinations(range(0, 10), i):
    comb = list(comb)
    comb.sort(reverse=True)
    s.append(int(''.join(map(str, comb))))
    
s.sort()

try:
  print(s[n])
except:
  print(-1)