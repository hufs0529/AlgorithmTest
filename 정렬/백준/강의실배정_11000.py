n = int(input())
s = []
room = 1

stack = []

for _ in range(n):
    a, b = map(int, input().split())
    stack.append((a, 1))
    stack.append((b, -1))
stack.sort(key=lambda x: (x[0], x[1]))

maxroom = 0
room = 0
for time, n in stack:
    room += n
    if room > maxroom:
        maxroom = room

print(maxroom)