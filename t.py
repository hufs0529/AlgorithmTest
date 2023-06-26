n = int(input())
s = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if s[stack[-1][0]] < s[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][0] + 1
            break
    stack.append((i, s[i]))
print(*answer)
