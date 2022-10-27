import heapq
heap = []
s = []
n = int(input())

for _ in range(n):
  s.append(list(map(int, input().split())))
  
  if not heap:
    for s1 in s:
      heapq.heappush(heap, s1)
  else:
    for s1 in s:
      if heap[0] < s1:
        heapq.heappop(heap)
        heapq.heappush(heap, s1)
        
        
print(heap[0])