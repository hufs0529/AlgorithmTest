def dfs(start, depth):
  if depth == 6:
    for i in range(6):
      print(comb[i], end=' ')
    print()
    return
  for i in range(start, len(s)):
    comb[depth] = s[i]
    dfs(i+1, depth+1)
comb = [0 for i in range(13)]

while True:
  s = list(map(int, input().split()))
  if s[0] == 0:
    break
  del s[0]
  dfs(0, 0)
  print()
  