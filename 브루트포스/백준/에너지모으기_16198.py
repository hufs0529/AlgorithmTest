n = int(input())
marble = list(map(int, input().split()))
total = 0

while n > 2:
    max_sum = 0
    max_index = -1

    for i in range(1, n-1):
        cur = marble[i-1] * marble[i+1]
        if cur > max_sum:
            max_sum = cur
            max_index = i

    total += max_sum
    del marble[max_index]
    n -= 1

print(total)

# 1 2 3 4
# 1 2 4 / n=3, sum = 8
# 1 4 /n=2, sum = 12