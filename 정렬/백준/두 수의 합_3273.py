n = int(input())
s = list(map(int, input().split()))
x = int(input())
s.sort()
start, end = 0, n-1
ans = 0

while start < end:
    tmp = s[start] + s[end]
    if tmp == x:
        ans += 1
    if tmp < x:
        start += 1
    else:
        end -= 1
print(ans)