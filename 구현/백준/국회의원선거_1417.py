n = int(input())
s = []
for _ in range(n):
  s.append(int(input()))
top = s[0]
del s[0]
s.sort(reverse=True)
cnt = 0

if n == 1:
  print(0)
else:
  while top <= s[0]:
    top += 1
    cnt += 1
    s[0] -= 1
    s.sort(reverse=True)
print(cnt)