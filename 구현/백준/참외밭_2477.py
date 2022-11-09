n = int(input())
s = []
for _ in range(6):
  a, b = map(int, input().split())
  s.append([a, b])

w, w_idx, h, h_idx = 0, 0, 0, 0
for i in range(len(s)):
  if s[i][0] == 1 or s[i][0] == 2:
    if w < s[i][1]:
      w = s[i][1]
      w_idx = i
  elif s[i][0] == 3 or s[i][1] == 4:
    if h < s[i][1]:
      h = s[i][1]
      h_idx = i
      
subW = abs(s[(w_idx - 1)%6][1] - s[(w_idx + 1)%6][1])
subH = abs(s[(h_idx - 1)%6][1] - s[(h_idx + 1)%6][1])
ans = ((w*h) - (subW - subH))*n
print(ans)            