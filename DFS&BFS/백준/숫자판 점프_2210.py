dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

s = []
result = []
for _ in range(5):
  s.append(list(map(str, input().split())))
  
def dfs(x, y, number):
  if len(number) == 6:
    if number not in result:
      result.append(number)
      
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 5 and 0 <= ny < 5:
      dfs(nx, ny, number + s[nx][ny])
      
for i in range(5):
  for j in range(5):
    dfs(i, j, s[i][j])

print(len(result))