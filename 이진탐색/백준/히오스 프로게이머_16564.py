n, k = map(int, input().split())
levels = []
for _ in range(n):
    levels.append(int(input()))

levels.sort()
start = levels[0]
end = levels[-1] + k
res = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for level in levels:
        if mid > level:
            sum += (mid - level)
    
    if sum <= k:
        start = mid + 1
        res = max(res, mid)
    else:
        end = mid - 1
print(res)