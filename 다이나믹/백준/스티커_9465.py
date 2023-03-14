t = int(input())

for _ in range(t):
    s = []
    n = int(input())
    for _ in range(2):
        s.append(list(map(int, input().split())))
    for i in range(1, n):
        if i == 1:
            s[0][i] += s[1][i-1]
            s[1][i] += s[0][i-1]
        else:
            s[0][i] += max(s[1][i-1], s[1][i-2])
            s[1][i] += max(s[0][i-1], s[0][i-2])
            
    print(max(s[0][n-1], s[1][n-1]))