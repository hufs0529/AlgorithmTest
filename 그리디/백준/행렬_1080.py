dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())

graph = [list(map(int,list(input()))) for _ in range(n)]
ideal = [list(map(int,list(input()))) for _ in range(n)]
  
def reverse(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      graph[i][j] = 1 - graph[i][j]
      
def check():
  for i in range(n):
    for j in range(m):
      if graph[i][j] != ideal[i][j]:
        return False
  return True

cnt = 0

for i in range(n-2):
  for j in range(m-2):
    if graph[i][j] != ideal[i][j]:
      reverse(i, j)
      cnt += 1
      
if check():
  print(cnt)
else:
  print(-1)