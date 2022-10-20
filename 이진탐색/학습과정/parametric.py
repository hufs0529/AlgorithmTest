n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start=0
total = 0
end=max(array)
mid = (start + end)//2

while start<=end:
  for i in array:
    if i > mid:
      total += (i - mid)
  
  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1
print(result)