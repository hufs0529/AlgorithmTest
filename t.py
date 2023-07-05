<<<<<<< HEAD
n = int(input())
s = list(map(int, input().split()))
stack, answer = [], []

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
=======
n, m = map(int, input().split())
prefix_sum = [0]
s = list(map(int, input().split()))
tmp = 0

for i in s:
    tmp += i
    prefix_sum.append(tmp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])
>>>>>>> 2aff011a2e0ebb9aeb1217d2191d92180f7489a7
