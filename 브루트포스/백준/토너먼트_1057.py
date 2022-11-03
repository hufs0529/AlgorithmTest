n , kim, lim = map(int, input().split())
round = 0
while kim != lim:
  kim -= kim // 2
  lim -= lim // 2
  round += 1
print(round)