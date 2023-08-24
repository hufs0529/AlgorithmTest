n = int(input())
heap = []
s = [[0]*2 for _ in range(n)]
for i in range(n):
    start, end = map(int, input().split())
    s[i][0] = start
    s[i][1] = end

s.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end_time = s[0][1]
for i in range(1, n):
    if s[i][0] >= end_time:
        cnt += 1
        end_time = s[i][1]
print(cnt)