from bisect import bisect_left

n, h = map(int, input().split())
down, up = [], []

for i in range(n):
	if i%2 == 0:
		down.append([int(input())])
	else:
		up.append([int(input())])

down.sort()
up.sort()
cnt = 1

min_val = 1e9
for i in range(1, h+1):
	t, b = bisect_left(up, (h+1)-i), bisect_left(down, i)
	total = n - (t+b)
	if total < min_val:
		min_val = total
		cnt = 1
	elif total == min_val:
		cnt += 1
