n, s = map(int, input().split())
sequence = list(map(int, input().split()))
min_val = n+1
left, right, sum = 0, 0, 0

while True:
    if sum >= s:
        min_val = min(min_val, right-left)
        sum -= sequence[left]
        left += 1
    elif right == n:
        break
    else:
        sum += sequence[right]
        right += 1

print(min_val)