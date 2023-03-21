import heapq

n = int(input())
s = []
res = 0
for _ in range(n):
  heapq.heappush(s, int(input()))
  
if len(s) == 1:
  print(0)
else:
  while len(s) > 1:
    plus = heapq.heappop(s) + heapq.heappop(s)
    res += plus
    heapq.heappush(s, plus)
    
  print(res)