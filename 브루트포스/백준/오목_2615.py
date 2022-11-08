dx = [1, 1, 0, -1]  # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1] 

board = []
n = 19
for _ in range(n):
  board.append(list(map(int, input().split())))
  
def omok():
  for x in range(n):
    for y in range(n):
      if board[x][y]:
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          cnt = 1
          
          while 0 <= nx < n and 0 <= ny < n and board[x][y] == board[nx][ny]:
            cnt += 1
            if cnt == 5:
              if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and board[nx][ny] == board[nx + dx[i]][ny + dy[i]]:  # 육목 판정 1
                break
              if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and board[x][y] == board[x - dx[i]][y - dy[i]]:  # 육목 판정 2
                break
              return board[x][y], x+1, y+1
            
            nx += dx[i]
            ny += dy[i] 
  return 0, -1, -1

color, x, y = omok()
if not color:
  print(color)
else:
  print(color)
  print(x, y)