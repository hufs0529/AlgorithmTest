from itertools import combinations

L, C = map(int, input().split())
vowels = ['a','e','o','u']
chars = sorted(list(map(str, input().split())))
res = 0

for c in list(combinations(chars, L)):
  vo, co = 0, 0
  for char in c:
    if char in vowels:
      vo += 1
    else:
      co += 1
  if vo > 0 and co > 1:
    res.append(''.join(c))
    
    