cal = input().split('-') # 55/50+40/10+30
tmp = []

for c in cal:
    sum = 0
    t = c.split('+')
    for i in t:
        sum += int(i)
    tmp.append(sum)

n = tmp[0]
for i in range(1, len(tmp)):
    n -= tmp[i]

print(n)