n = int(input())
s = []
for i in range(n):
    c, s = map(int, input().split())
    s.append([i, c, s])


s.sort(key=lambda x:(x[1], x[2]))
color_list = [0] * 200001
player_list = [0] * n

sum_ = 0
i, j = 0, 0

while i < n:
    a_ball = s[i]
    b_ball = s[j]
    while b_ball[1] < a_ball[1]:
        sum_ += b_ball[1]
        color_list[b_ball[2]] += b_ball[1]
        
        j += 1
        b_ball = s[j]
    
    s[a_ball[0]] = sum_ - color_list[a_ball[2]]
    i += 1
    
result = []
for i in range(n):
    result.append(str(player_list[i]))
print('\n'.join(result))
    
    
# 3 15
# 1 10
# 4 8
# 1 3