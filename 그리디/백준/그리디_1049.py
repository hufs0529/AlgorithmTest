n, m = map(int, input().split())
six_list = []
one_list = []
money = 0
nMin = 1e9

for _ in range(m):
  a, b = map(int, input().split())
  six_list.append(a)
  one_list.append(b)
six_list.sort()
one_list.sort()
  
  
if six_list[0] <= one_list[0] * 6:
  money = six_list[0] * (n // 6) + one_list[0] * (n%6)
  if six_list[0] < one_list[0] * (n % 6):
    money = six_list[0] * (n//6 + 1)
else:
  money = one_list[0] * n
  
print(money)