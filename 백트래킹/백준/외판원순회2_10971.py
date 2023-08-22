n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
min_val = 1e9

def dfs(start, next, value, visited):
    global min_val
    if len(visited) == n:
        if s[next][start] != 0:
            min_val = min(min_val, value + s[next][start])
        return
    for i in range(n):
        if s[next][i] != 0 and i not in visited and value < min_val:
            visited.append(i)
            dfs(start, i, value + s[next][i], visited)
            visited.pop()

for i in range(n):
    dfs(i, i, 0, [i])
print(min_val)