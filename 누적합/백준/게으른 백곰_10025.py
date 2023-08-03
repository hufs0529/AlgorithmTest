import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] * 1000001
max_location = 0
for _ in range(n):
    g, x = map(int, input().split())
    s[x] = g
    max_location = max(max_location, x)

step = 2*k+1

window = sum(s[:step])
answer = window

for i in range(k+1, max_location - k +1):
    window += s[i] - s[i-step]
    answer = max(answer, window)
print(answer)