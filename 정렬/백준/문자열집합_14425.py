n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())
cnt = 0
for i in range(m):
    t = input()
    if t in s:
        cnt += 1
print(cnt)