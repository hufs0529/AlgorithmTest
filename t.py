from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

def bfs(a, b):
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 2:
				queue.append((i, j))
	
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < m and graph[nx][n] == 0:
				graph[nx][ny] = 2
				queue.append([nx, ny])
	
	global result
	cnt = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] == 0:
				cnt += 1
	result = max(result, cnt)


result = 0