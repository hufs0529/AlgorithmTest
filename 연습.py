N, L = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]
pool.sort(key=lambda x: x[0])
plank = pool[0][0]
total = 0

for start, end in pool:
  if plank > end:
    continue
  elif plank < start:
    plank = start
    
  dist = end - plank
  remainder = 1
  if dist % L == 0:
    remainder = 0
  count = dist // L + remainder
  plank += count * L
  total += count
print(total)