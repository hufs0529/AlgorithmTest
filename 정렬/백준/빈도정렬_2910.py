n, c = map(int, input().split())
seq = list(map(int, input().split()))
dict = {}
idx = 1

for s in seq:
    if s in dict:
        dict[s][0] += 1
    else:
        dict[s] = [1, idx]
        idx += 1

numbers = sorted(dict.items(), key=lambda x:(-x[1][0], x[1][1]))
res = []
for i,j in numbers:
    res += [i]*j[0]
print(*res)