n, k = map(int, input().split())
s = list(map(int, input().split()))
cnt = 0
check = [0]*n
  
def dfs(depth, t):
  global cnt
  if depth == n:
    cnt += 1
    return
  for i in range(n):
    if check[i] or t + s[i] - k < 0:
      continue
    check[i] = 1
    dfs(depth+1, t+s[i] - k)
    check[i] = 0
    
dfs(0, 0)
print(cnt)