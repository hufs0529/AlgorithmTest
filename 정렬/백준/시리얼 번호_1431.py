n = int(input())

def sum_num(inputs):
  res = 0
  for i in inputs:
    if i.isdigit():
      res += int(i)
  return res

s = []
for i in range(n):
  a = input()
  s.append(a)
  
s.sort(key=lambda  x:(len(x),sum_num(x) ,x))

for i in s:
  print(i)