n, m = map(int, input().split())
s = [[] for _ in range(n)]
visited = [False] * 2001
for _ in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)
ans = False

def dfs(idx, depth):
    global ans
    visited[idx] = True
    if depth == 4:
        ans = True
        return

    for i in s[idx]:
        if not visited[idx]:
            visited[i] = True
            dfs(i, depth+1)
            visited[i] = False


for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)