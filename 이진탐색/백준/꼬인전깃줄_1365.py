from bisect import bisect_left

n = int(input())
s = list(map(int, input().split()))
res = [s[0]]

for i in range(1, n):
    index = bisect_left(res, s[i])
    if index == len(res):
        res.append(s[i])
    else:
        res[index] = s[i]
print(len(s) - len(res))