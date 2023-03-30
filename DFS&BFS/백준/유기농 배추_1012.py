t = int(input())

def dfs(x, y):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        dfs(nx, ny)

for _ in range(t):
  cnt = 0
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  
  for j in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1
  
  for a in range(n):
    for b in range(m):
      if graph[a][b] == 1:
        dfs(x, y)
        cnt += 1
  print(cnt)