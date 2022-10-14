n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(input()))
  
cnt = 0

# -확인
for i in range(n):
  pre = '/'
  for j in range(m):
    if board[i][j] == '-':
      if pre != board[i][j]:
        cnt += 1
      pre = board[i][j]
      
# |확인
for j in range(m):
  pre = '/'
  for i in range(n):
    if board[i][j] == '|':
      if pre != board[i][j]:
        cnt += 1
      pre = board[i][j]
      
print(cnt)