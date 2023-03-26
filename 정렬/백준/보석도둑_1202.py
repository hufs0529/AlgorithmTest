import heapq

n, k = map(int, input().split())

jewel_info = []
for _ in range(n):
  m, v = map(int, input().split())
  heapq.heappush(jewel_info, [m, v])

pack_weight = []
for _ in range(k):
  pack_weight.append(int(input()))
pack_weight.sort()

answer = 0
tmp_jew = []
for bag in pack_weight:
  while jewel_info and bag >= jewel_info[0][0]:
    heapq.heappush(tmp_jew, -heapq.heappop(jewel_info)[1])
  if tmp_jew:
    answer -= heapq.heappop(tmp_jew)
  elif not jewel_info:
    break
print(answer)