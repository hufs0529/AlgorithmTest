def dfs(s, t):
    while len(t) >= len(s):
        if t == s:
            return True
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[:-1][::-1]
    return False

s = input()
t = input()

if dfs(s, t):
    print(1)
else:
    print(0)