from collections import deque

n = int(input())
m = int(input())
visited = [False] * (n+1)
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
	queue = deque([x])
	cnt = 0
	visited[x] = True
	while queue:
		q = queue.popleft()
		for i in graph[q]:
			if not visited[i]:
				visited[i] = True
				queue.append(i)
				cnt += 1
	return cnt

print(bfs(1))