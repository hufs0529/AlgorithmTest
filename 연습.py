from itertools import combinations_with_replacement

n = int(input())
ans = set()
lst = [1, 5, 10, 50]

for comb in combinations_with_replacement(lst, n):
  ans.add(sum(comb))
print(len(ans))