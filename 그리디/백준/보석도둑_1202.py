import heapq

n, k = map(int, input().split())
jew = []
for _ in range(n):
    heapq.heappush(jew, list(map(int, input().split())))
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()

answer = 0
tmp = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])
    if tmp:
        answer -= heapq.heappop(tmp)
    elif not tmp:
        break
print(answer)