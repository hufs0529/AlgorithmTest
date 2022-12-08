n = int(input())
s = []
for _ in range(n):
    n, d, m, y = input().split()
    d, m, y = map(int, (d,m,y))
    s.append((y,m,d,n))
    
s.sort()
print(s[-1][3])
print(s[0][3])