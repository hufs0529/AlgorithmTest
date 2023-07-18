dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
board = []
for _ in range(r):
	board.append(list(input()))
ans = 0
alpha = set()

def dfs(x, y, count):
	global ans
	ans = max(ans, count)
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in alpha:
			alpha.add(board[nx][ny])
			dfs(nx, ny, count+1)
			alpha.remove(board[nx][ny])

alpha.add(board[0][0])
dfs(0,0,1)
print(ans)