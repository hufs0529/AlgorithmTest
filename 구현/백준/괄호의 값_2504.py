shields = list(input())
score = 0
stack = []
tmp = 1

for i in range(len(shields)):
  if shields[i] == '(':
    tmp *= 2
    stack.append(shields[i])
  elif shields[i] == '[':
    tmp *= 3
    stack.append(shields[i])
  
  elif shields[i] == ')':
    if not stack or stack[-1] == '[':
      score = 0
      break
    if shields[i-1] == '(':
      score += tmp
    stack.pop()
    tmp //= 2
    
  else:
    if not stack or stack[-1] == '(':
      score = 0
      break
    if shields[i-1] == '[':
      score += tmp
    stack.pop()
    tmp //= 3
    
if stack:
  print(0)
else:
  print(score)