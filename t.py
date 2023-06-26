shields = input()
stack = []
ans = 0
tmp = 1

for i in range(len(shields)):
    if shields[i] == "(":
        tmp *= 2
        stack.append(shields[i])
    elif shields[i] == "[":
        tmp *= 3
        stack.append(shields[i])
    elif shields[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if shields[i - 1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2
    elif shields[i] == "]":
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if shields[i - 1] == "[":
            ans += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)
