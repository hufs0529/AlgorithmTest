n, d, k, c = map(int, input().split())
s = []
for _ in range(n):
  s.append(int(input()))
answer = 0, 0
lp, rp = 0, 0

while lp != n:
  rp = lp + k
  case = set()
  addable = True
  for i in range(lp, rp):
    i %= n
    case.add(s[i])
    if s[i] == c:
      addable = False
  
  cnt = len(case)
  if addable:
    cnt += 1
  answer = max(answer, cnt)
  lp += 1

print(answer)