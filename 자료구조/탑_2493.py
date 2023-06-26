n = int(input())
s = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > s[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, s[i]])

print(" ".join(map(str, answer)))
