vowels = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())
s = sorted(list(map(str, input().split())))
ans = []

def dfs(cnt, idx):
    if cnt == l:
        vo, co = 0, 0
        for i in range(l):
            if ans[i] in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(map(str, ans)))
    
    for i in range(idx, c):
        ans.append(s[i])
        dfs(cnt+1, i+1)
        ans.pop()
dfs(0, 0)