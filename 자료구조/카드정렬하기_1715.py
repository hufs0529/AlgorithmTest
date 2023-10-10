import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

if len(heap) == 1:
    print(0)
else:
    answer = 0
    while len(heap) > 1:
        t1 = heapq.heappop(heap)
        t2 = heapq.heappop(heap)
        answer += (t1 + t2)
        heapq.heappush(heap, t1+t2)
    print(answer)