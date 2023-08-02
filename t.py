n, k = map(int, input().split())
s = []
max_val = -1
for i in range(n):
    # 첫번째 얼음 무게, 두번째 위치
    s.append(list(map(int, input().split())))
    max(max_val, s[i][1])

sorted_s = sorted(s, key=lambda x:x[1])
ans = 0
start, end = 0, max_val

while start <= end:
    gram = 0
    mid = (start+end)//2
    range_l, range_r = mid - k, mid + k
    for s in sorted_s:
        if range_l <= s[1] <= range_r:
            gram += s[1]
    
    if gram >= ans:
        ans = gram
        start = mid + 1
    else:
        end = mid - 1
print(ans)