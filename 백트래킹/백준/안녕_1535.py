n = int(input())
cost = list(map(int, input().split()))
joy = list(map(int, input().split()))
ans = 0

def dfs(idx, cur_joy, cur_life):
    global ans

    if cur_life <= 0:
        prev_joy = cur_joy - joy[i-1]
        if prev_joy > ans:
            ans = prev_joy
        return

    if idx == n:
        if cur_joy > ans:
            ans = cur_joy
        return

    dfs(idx+1, cur_joy + joyo[idx], cur_life - cost[idx])
    dfs(idx+1, cur_joy, cur_life)

dfs(0, 0, 100)
print(ans)