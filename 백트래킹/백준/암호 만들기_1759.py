l, c = map(int, input().split())
words = sorted(list(input().split()))
ans = []
vowels = ['a','e','i','o','u']

def dfs(depth, idx):
    if depth == l:
        vo, co = 0, 0
        for i in range(l):
            if ans[i] in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(ans))
        return

    for i in range(idx, c):
        ans.append(words[i])
        dfs(depth+1, i+1)
        ans.pop()

dfs(0, 0)