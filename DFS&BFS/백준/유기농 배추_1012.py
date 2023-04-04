t = int(input())

def dfs(x, y):
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if graph[nx][ny] == 1:
        dfs(nx, ny)
        graph[nx][ny] = 0
        

for _ in range(t):
  cnt = 0
  m, n, k = map(int, input().split())
  graph = [[0] * (n) for _ in range(m)]
  
  for j in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
  
  for a in range(m):
    for b in range(n):
      if graph[a][b] == 1:
        dfs(x, y)
        cnt += 1
  print(cnt)
  
  