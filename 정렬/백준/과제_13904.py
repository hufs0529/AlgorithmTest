n = int(input())
s = []
visit = [False] * 1001

for i in range(n):
    a, b = map(int, input().split())
    s.append([a, b])
s.sort(key=lambda x: x[1], reverse=True)
ans = 0
for day, worth in s:
    i = day
    while i > 0 and visit[i]:
        i -= 1
    if i == 0:
        continue
    else:
        visit[i] = True
        ans += worth

print(ans)  

# 4 60
# 2 50
# 4 40
# 3 30
# 1 20
# 4 10
# 6 5

# 1 20
# 2 50
# 3 30
# 4 10
# 4 40
# 4 60
# 6 5