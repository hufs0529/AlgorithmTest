n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))

start, end = min(s), max(s)  # 100 500

while start <= end:
    mid = (start + end) // 2
    charge = mid
    num = 1
    for i in s:
        if i >= charge:
            charge = mid
            num += 1
        charge -= i

    if num > m or mid < max(s):
        start = mid + 1
    else:
        end = mid - 1
        k = mid

print(k)
