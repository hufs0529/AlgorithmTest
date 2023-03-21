n = int(input())

s = list(map(int, input().split()))
dp1 = [1] * n
dp2 = [1] * n
sub_len = [0] * n

Max = 0

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
 
s.reverse()

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp2.reverse()

for i in range(n):
    sub_len[i] = dp1[i] + dp2[i]
    
print(max(sub_len)-1)