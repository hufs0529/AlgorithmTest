n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def dfs(start):
    if len(tmp) == m:
        print(*tmp)
        return
    for i in range(start, n):
        tmp.append(nums[i])
        dfs(i)
        tmp.pop()

dfs(0)