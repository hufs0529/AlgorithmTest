from itertools import combinations

n = int(input())
s = []
com = []
for _ in range(n):
  s.append(list(map(int, input().split())))

ans = 1e9
for i in range(1, n+1):
  com.append(combinations(s, i))
  
for line in com:
  for each in line:
    sour = 1
    bitter = 0
    for e in each:
      sour *= e[0]
      bitter += e[1]
    ans = min(ans, abs(sour - bitter))
    
print(ans)