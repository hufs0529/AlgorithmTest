from bisect import bisect_left

n, H = map(int, input().split())
cave = [int(input()) for _ in range(n)]

top, bot = [], []
for i in range(n):
    if i % 2 == 0:
        bot.append(cave[i])
    else:
        top.append(cave[i])

top.sort()
bot.sort()
cnt = 1
min_val = float("inf")
for h in range(1, H + 1):
    t, b = bisect_left(top, (H + 1) - h), bisect_left(bot, h)
    total = n - (t + b)
    if total < min_val:
        min_val = total
        cnt = 1
    elif total == min_val:
        cnt += 1

print(min_val, cnt)
