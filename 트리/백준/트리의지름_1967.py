from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
max_node = -1

def bfs(start):
    global n, max_node
    queue = deque([[start, 0]])
    visited = [False] * (n+1)
    visited[start] = True
    max_dist = 0
    
    while queue:
        now, now_dist = queue.popleft()
        for child, child_dist in graph[now]:
            if not visited[child]:
                visited[child] = True
                queue.append([child, child_dist+now_dist])
                if max_dist < child_dist+now_dist:
                    max_dist = child_dist+now_dist
                    max_node = child
    return max_dist

bfs(1)
print(bfs(max_node))