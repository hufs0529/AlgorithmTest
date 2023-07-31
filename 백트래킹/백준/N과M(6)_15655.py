n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
ans = []

def dfs(start):
    if m == len(ans):
        print(*ans)
        return

    for i in range(start, n):
        if s[i] not in ans:
            ans.append(s[i])
            dfs(i+1)
            ans.pop()

dfs(0)