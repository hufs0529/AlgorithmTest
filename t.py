n, m = map(int, input().split())
s = []
for _ in range(n):
	s.append(int(input()))

start, end = min(s), max(s)

while start <= end:
	mid = (start + end) // 2
	charge = mid
	num = 1
	for i in range(n):
		if charge < s[i]:
			charge = mid
			num += 1
		charge -= s[i]
	
	if num > m or mid < max(s):
		start = mid + 1
	else:
		end = mid - 1
		k = mid
print(k)