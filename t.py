n, m = map(int, input().split())
lines = []
result = 0
for _ in range(m):
    a, b = map(int, input().split()) # 세트, 낱개 가격
    lines.append((a, b))

bulk = min(row[0] for row in lines)
indiv = min(row[1] for row in lines)

while n > 0:
    if n >= 6:
        result += bulk
        n -= 6
    else:
        result += indiv
        n -= 1

print(result)