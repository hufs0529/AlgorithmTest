n = int(input())
s = list(map(int, input().split()))
ans = [0] * n
for i in range(1, n+1):
  t = s[i-1]
  cnt = 0
  for j in range(n):
    if cnt == t and ans[j] == 0:
      ans[j] = i
      break
    elif ans[j] == 0:
      cnt += 1
print(*ans)