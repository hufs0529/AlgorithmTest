n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
ans = []

def dfs(start):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(start, n):
        ans.append(s[i])
        dfs(i)
        ans.pop()

dfs(0)