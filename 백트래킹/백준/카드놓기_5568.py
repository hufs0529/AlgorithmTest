def dfs(depth):
    if depth == k:
        comb.add("".join(map(str, tmp)))
        return

    for i in range(n):
        if check[i]:
            continue
        tmp.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        tmp.pop()
        check[i] = 0


n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
tmp, comb = [], set()
check = [0]*n
dfs(0)
print(len(comb))