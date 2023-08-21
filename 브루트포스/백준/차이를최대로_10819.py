from itertools import permutations

n = int(input())
s = list(map(int, input().split()))

permu = permutations(s)
ans = 0

for per in permu:
    s = 0
    for i in range(len(per) - 1):
        s += abs(per[i] - per[i+1])
    if s > ans:
        ans = s
print(ans)