n, m = map(int, input().split())
s = list(map(int, input().split()))

start, end = 0, max(s)
res = 0

while start <= end:
  mid = (start + end)//2
  tot = 0
  for i in s:
    if i >= mid:
      tot += (i // mid)
      
  if tot >= n:
    start = mid + 1
    res = mid
  else:
    end = mid - 1
print(res)