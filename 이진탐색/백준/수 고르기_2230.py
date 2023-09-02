n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))
s.sort()

left, right = 0, 0
result = int(2e9)

while left <= right and right < n:
    if s[right]-s[left]< m:
        right += 1
    else:
        result = min(result, s[right]-s[left])
        left += 1

print(result)