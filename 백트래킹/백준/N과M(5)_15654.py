n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
tmp = []

def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    
    for i in range(n):
        if s[i] in tmp:
            continue
        tmp.append(s[i])
        dfs()
        tmp.pop()

dfs()