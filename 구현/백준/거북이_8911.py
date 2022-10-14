dl = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]
dirL = [2, 3, 1, 0]
dirR = [3, 2, 0, 1]

t = int(input())
for _ in range(t):
  word = input()
  min_r, min_l, max_r, max_l = 0, 0, 0, 0
  direction, r, l = 0, 0, 0
  
  for i in word:
    if i == 'L':
      direction = dirL[direction]
    elif i == 'R':
      direction = dirR[direction]
    elif i == 'F':
      r += dr[direction]
      l += dl[direction]
    elif i == 'B':
      r -= dr[direction]
      l -= dl[direction]
      
    min_r = min(min_r, r)
    min_l = min(min_l, l)
    max_r = max(max_r, r)
    max_l = max(max_l, l)

  print(abs(max_r - min_r) * abs(max_l - min_l))