from itertools import permutations

n = int(input())
s = list(map(int, input().split()))

per = permutations(s)
ans = 0

for i in per:
  tmp = 0
  for j in range(len(i) - 1):
    tmp += abs(i[j] - i[j+1])
  if tmp > ans:
    ans = tmp
    
print(ans)