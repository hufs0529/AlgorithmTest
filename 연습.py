n = int(input())
s = {}

for _ in range(n):
    num = int(input())
    if num in s:
        s[num] += 1
    else:
        s[num] = 1
        
result = sorted(s.items(), key=lambda x:(-x[1],x[0]))
print(result[0][0])   