import sys

input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    a, b = map(int, input().split())
    s.append([a, b])
s.sort(key=lambda x: (x[0], x[1]))

start = s[0][0]
end = s[0][1]
ans = 0

for i in range(1, n):
  cur_start, cur_end = s[i]
  
  if cur_start < end:
    end = max(end, cur_end)
  else:
    ans += (end - start)
    start, end = cur_start, cur_end
    
ans += (end - start)
print(ans)