n = int(input())
s = []
min_value = 1e9

for _ in range(n):
    a, b, c = map(int, input().split())
    s.append([a, b, c])

for i in range(1, n):
    s[i][0] = min(s[i - 1][1], s[i - 1][2]) + s[i][0]
    s[i][1] = min(s[i - 1][0], s[i - 1][2]) + s[i][1]
    s[i][2] = min(s[i - 1][0], s[i - 1][1]) + s[i][2]

print(min(s[n - 1]))
