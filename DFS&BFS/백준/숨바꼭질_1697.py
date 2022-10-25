from collections import deque

def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    q = queue.popleft()
    if q == k:
      print(dist[q])
      break
    for nx in (q-1, q+1, q*2):
      if 0 <= nx <= MAX and not dist[nx]:
        dist[nx] = dist[q]+1
        queue.append(nx)

MAX = 10**5
dist = [0] * (MAX+1)
n, k = map(int, input().split())

bfs()