n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]
Max, candy = 0, 0

def dfs(x, y, candy, visited):
  global Max
  if x == n-1 and y == m-1:
    candy += s[x][y]
    if Max < candy:
      Max = candy
    return
  
  if 0 <= x < n and 0 <= y < m and visited[x][y] == 0:
    visited[x][y] = 1
    dfs(x+1, y, candy+s[x][y],visited)
    dfs(x,y+1,candy+s[x][y],visited)
    dfs(x+1,y+1,candy+s[x][y],visited)
    
dfs(0,0,candy,visited)
print(Max)