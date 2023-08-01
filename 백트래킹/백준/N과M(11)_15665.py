n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    
    history = 0
    for i in range(n):
        if history != s[i]:
            temp.append(s[i])
            history = s[i]
            dfs()
            temp.pop()

dfs()