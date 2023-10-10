import heapq
heap = []
n = int(input())
for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
