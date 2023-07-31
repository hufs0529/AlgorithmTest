n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
ans = []
visited = [False]

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    history = 0

    for i in range(n):
        if not visited[i] and history != s[i]:
            visited[i] = True
            ans.append(s[i])
            history = s[i]
            dfs()
            visited[i] = False
            ans.pop()

dfs()