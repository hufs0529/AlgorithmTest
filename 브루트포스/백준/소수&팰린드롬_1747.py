n = int(input())
res = 0

def primeNumber(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for num in range(n, 1000001):
  if num == 1:
    continue
  
  if str(num) == str(num)[::-1]:
    if primeNumber(num) == True:
      res = num
      break
    
if res == 0:
  res = 1003001 
print(res)