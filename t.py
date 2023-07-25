n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))

start, end = min(time), max(time) * m
ans = end

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        total += mid // time[i]
    
    if total >= m:
        end = mid - 1
        ans = min(ans, mid)
    else:
        start = mid + 1
        
print(ans)