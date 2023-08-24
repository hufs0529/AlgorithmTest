n = int(input())
s = []
for _ in range(n):
    a, b = map(int, input().split())
    s.append([a, b])

s.sort(key=lambda x:(x[0], x[1]))

for i in s:
    print(*i)