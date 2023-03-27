from itertools import permutations

n = int(input())
s = list(map(int, input().split()))
ans = 0

for i in permutations(s):
  t = 0
  for j in range(1, n):
    t += abs(i[j-1] - i[j])
  if t > ans:
    ans = t
    
print(ans)