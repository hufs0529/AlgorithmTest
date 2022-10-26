from collections import deque

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def bfs(i, j):
  field[i][j] = 0
  queue = deque([i, j])
  while queue:
    x, y = queue.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
        field[nx][ny] = 0
        queue.append([nx, ny])
        
def dfs(x, y):
  field[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)
      
      
while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = []
  cnt = 0
  for _ in range(h):
    field.append(list(map(int, input().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        cnt += 1
    
print(cnt)