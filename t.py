n, m = map(int, input().split())
jewels = []
for _ in range(m):
    jewels.append(int(input()))

start, end = 1, max(jewels)
ans = end

while start <= end:
    mid = (start + end)//2
    tmp = 0
    for jewel in jewels:
        quot = jewel // mid
        remain = jewel % mid

        tmp += quot
        if remain > 0:
            tmp += 1

    if tmp > n:
        start = mid + 1
    else:
        ans = max(ans, mid)
        end = mid - 1

print(ans)