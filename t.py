n, m = map(int, input().split())
visited = [False] * n
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
ans = False

def dfs(idx, depth):
    global ans
    visited[idx] = True
    if depth == 4:
        ans = True
        return
    for i in friends[idx]:
        visited[idx] = True
        dfs(i, depth+1)
        visited[idx] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:break
if ans:
    print(1)
else:
    print(0)