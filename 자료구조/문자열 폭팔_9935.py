s1 = input()
s2 = input()
ex_len = len(s2)
stack = []

for i in range(len(s1)):
  stack.append(s1[i])
  
  if ''.join(stack[-ex_len:]) == s2:
    for _ in range(ex_len):
      stack.pop()
      
if stack:
  print(''.join(stack))
else:
  print('FRULA')