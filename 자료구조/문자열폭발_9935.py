a = input()
b = input()
stack = []
s_len = len(b)

for i in a:
    stack.append(i)
    #print(stack[-2:])
    if ''.join(stack[-s_len:]) == b:
        stack = stack[:-s_len]

ans = ''.join(stack) 
if ans == '':
    print('FRULA')
else:
    print(ans)