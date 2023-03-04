n = int(input())
s = list(map(int, input().split()))
s.sort()
ans = 0

for i in range(n):
    tmp = s[:i] + s[i+1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == s[i]:
            ans += 1
            break
        
        if t < s[i]:
            left += 1
        else:
            right -= 1
print(ans)