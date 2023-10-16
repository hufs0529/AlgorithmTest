a = input()
b = input()

stack = []
ex_len = len(b)

for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-ex_len:]) == b:
        for _ in range(ex_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')