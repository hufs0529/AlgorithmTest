<<<<<<< HEAD
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and field[nx][ny] == 1:
                field[nx][ny] = 2
                queue.append([nx, ny])


t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                field[i][j] = 0
                bfs(i, j)
                cnt += 1
    print(cnt)
=======
n, m = map(int, input().split())
s = []
for _ in range(n):
	s.append(int(input()))

start, end = min(s), max(s)

while start <= end:
	mid = (start + end) // 2
	charge = mid
	num = 1
	for i in range(n):
		if charge < s[i]:
			charge = mid
			num += 1
		charge -= s[i]

	if num > m or mid < max(s):
		start = mid + 1
	else:
		end = mid - 1
print(mid)
>>>>>>> d5c37c3e1a0d4ce58129789745ee1d48d23875fd
