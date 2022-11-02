from itertools import combinations

L, C = map(int, input().split())
chars = sorted(list(map(str, input().split())))
res = []
vowels = ['a','e','i','o','u']

for char in list(combinations(chars, L)):
  vc, cc = 0, 0
  for c in char:
    if c in vowels:
      vc += 1
    else:
      cc += 1
  if vc >0 and cc > 1:
    res.append(''.join(char))
    
for r in res:
  print(r)