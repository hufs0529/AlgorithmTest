n, m = map(int, input().split())
prefix_sum = [0]
s = list(map(int, input().split()))
tmp = 0

for i in s:
    tmp += i
    prefix_sum.append(tmp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])