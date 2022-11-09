shield = list(input())
stack = []
answer = 0
tmp = 1

for i in range(len(shield)):
  if shield[i] == '(':
    tmp *= 2
    stack.append(shield[i])
  elif shield[i] == '[':
    tmp *= 3
    stack.append(shield[i])
  elif shield[i] == ')':
    if not stack or stack[-1] == '[':
      answer = 0
      break
    if shield[i-1] == '(':
      answer += tmp
    stack.pop()
    tmp //= 2
  elif shield[i] == ']':
    if not stack or stack[-1] == '(':
      answer = 0
      break
    if shield[i-1] == '[':
      answer += tmp
    stack.pop()
    tmp //= 3
    
if stack:
  print(0)
else:
  print(answer)