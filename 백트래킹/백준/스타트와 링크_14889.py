8n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(n)]
min_val = 1e9

def back_tracking(depth, idx):
    global min_val
    if depth == n//2:
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    p2 += graph[i][j]
        min_val = min(min_val, abs(p1 - p2))


    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            back_tracking(depth+1, i+1)
            visited[i] = False

back_tracking(0, 0)
print(min_val)