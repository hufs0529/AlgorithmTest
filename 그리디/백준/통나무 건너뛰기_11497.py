t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, s[i] - s[i+2])
        
    print(result)