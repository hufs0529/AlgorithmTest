from collections import deque

n = int(input())
s = list(map(int, input().split()))
answer = [-1] * n
stack = deque()

for i in range(n):
    while stack and (stack[-1][0] < s[i]):
        tmp, idx = stack.pop()
        answer[idx] = s[i]
    stack.append([s[i], i])

print(*answer)