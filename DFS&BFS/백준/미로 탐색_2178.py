from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
s = []
for _ in range(n):
  s.append(list(map(int, input())))
  

def bfs(xx, yy):
  queue = deque()
  queue.append((xx, yy))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if s[nx][ny] == 1:
          s[nx][ny] = s[x][y] + 1
          queue.append((nx, ny))
          
  return s[n-1][m-1]

print(bfs(0, 0))