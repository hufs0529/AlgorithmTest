n = int(input())
cargo = []
for _ in range(n):
    a, b = map(int, input().split())
    cargo.append([a, b])
cargo.sort()
result = 0

i = 0
for c in cargo:
    if c[1] > result:
        result = c[1]
        idx = i
    i += 1
height = cargo[0][1]

for i in range(idx):
    if height < cargo[i+1][1]:
        result += height * (cargo[i+1][0] - cargo[i][0])
        height = cargo[i+1][1]
    else:
        result += height * (cargo[i+1][0] - cargo[i][0])

height = cargo[-1][1]

for i in range(n-1, idx, -1):
    if height < cargo[i-1][1]:
        result += height * (cargo[i][0] - cargo[i-1][0])
        height = cargo[i-1][1]
    else:
        result += height * (cargo[i][0] - cargo[i-1][0])

print(result)