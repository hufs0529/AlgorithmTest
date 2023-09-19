dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
cnt = 0

def dfs(x, y):
    global cnt
    if x == (n-1) and y == (m-1):
        print(cnt)
        return

    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]  

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
            visited[nx][ny] = True
            cnt += 1

            

dfs(0, 0)