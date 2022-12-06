n = int(input())
m = int(input())
s = list(map(int, input().split()))
s.sort()
cnt = 0
i, j = 0, n-1

while i < j:
    if s[i] + s[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif s[i] + s[j] < m:
        i += 1
    else:
        j -= 1
        
print(cnt)