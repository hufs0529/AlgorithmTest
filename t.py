n, m = map(int, input().split())
line = []
for _ in range(m):
    a, b = map(int, input().split())
    line.append([a, b])
ans = 0

st = sorted(line, key=lambda x:x[0])
each = sorted(line, key=lambda x:x[1])

if st[0][0] <= each[0][1] * 6: # 세트 가격이 낱개 6개보다 저렴할때
    ans = st[0][0] * (n//6) + each[0][1] * (n%6)
else: # 세트 가격이 낱개 6개보다 비쌀때
    ans = each[0][1] * n

print(ans)
