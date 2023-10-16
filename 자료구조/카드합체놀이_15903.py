import heapq

n, m = map(int, input().split())
s = list(map(int, input().split()))
heap = []
for i in s:
    heapq.heappush(heap, i)

for i in range(m):
    t1 = heapq.heappop(heap)
    t2 = heapq.heappop(heap)
    tmp = t1 + t2
    for i in range(2):
        heapq.heappush(heap, tmp)

print(sum(heap))

# 4 3 3 3
# 4 6 6 3