n, m = map(int, input().split())
jewels = []
for _ in range(m):
  jewels.append(int(input()))
  
start, end = 1, max(jewels)
answer = end

while start <= end:
  mid = (start + end) // 2
  person = 0
  
  for jewel in jewels:
    mok = jewel // mid
    namo = jewel % mid
    
    person += mok
    if namo > 0:
      person += 1
      
  if person > n:
    start = mid + 1
  else:
    answer = min(answer, mid)
    end = mid - 1
    
print(answer)