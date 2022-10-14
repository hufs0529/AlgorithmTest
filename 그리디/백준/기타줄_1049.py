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
six = six_list[0]
one = one_list[0]
  
if six <= one * 6:
  money = six * (n // 6) + one * (n % 6)
  if six < one * (n % 6):
    money = six * (n//6 + 1)
else:
  money = one * n
  
print(money)