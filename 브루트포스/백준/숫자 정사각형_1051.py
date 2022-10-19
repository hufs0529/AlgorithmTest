n, m = map(int, input().split())
min_nm = min(n, m)
s = []
tmp = 0

for _ in range(n):
  s.append(list(input()))
  
for i in range(n):
  for j in range(m):
    for k in range(min_nm):
      if ((i+k) < n) and ((j+k) < m) and (s[i][j] == s[i][j+k] == s[i+k][j] == s[i+k][j+k]):
        tmp = max(tmp, (k+1)**2)
        
print(tmp)