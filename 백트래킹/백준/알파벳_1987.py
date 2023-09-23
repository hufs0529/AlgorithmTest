dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))

alphas = set()
ans = 0

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, cnt + 1)
            alphas.remove(maps[nx][ny])

alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)