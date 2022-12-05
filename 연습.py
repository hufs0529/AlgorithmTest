import heapq

n = int(input())
s = []
heap = []

for _ in range(n):
    s.append(list(map(int, input().split())))
    
    if not heap:
        for s1 in s:
            heapq.heappush(heap, s1)
    else:
        if heap[0] < s1:
            heapq.heappop()
            heapq.heappush(heap, s1)