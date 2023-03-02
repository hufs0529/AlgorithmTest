n = int(input())
s = list(map(int, input().split()))
s.sort()
final = []

left, right = 0, n-1
answer = 1e9

while left < right:
    s_left = s[left]
    s_right = s[right]
    
    tot = s_left + s_right
    
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
        
    if tot < 0:
        left += 1
    else:
        right -= 1
        
    
print(final[0], final[1])    
    