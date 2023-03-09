n = int(input())
s = list(map(int, input().split()))
s.sort()
x = int(input())
ans = 0

start, end = 0, n-1
while start < end:
    tmp = s[start] + s[end]
    
    if tmp == x:
        ans += 1
    if tmp < x:
        start += 1
        continue
    else:
        end -= 1
        
print(ans)