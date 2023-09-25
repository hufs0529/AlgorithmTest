n, s = map(int, input().split())
nums = list(map(int, input().split()))
min_val = 1e9
left, right = 0, 0
sum = 0

while True:
    if sum >= s:
        min_val = min(min_val, right - left)
        sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        sum += nums[right]
        right += 1

print(min_val)