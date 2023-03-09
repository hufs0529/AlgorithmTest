n = int(input())
k = int(input())
s = list(map(int, input().split()))
s.sort()

arr = []
for i in range(n-1):
    arr.append(s[i+1] - s[i])
    
arr.sort()

print(sum(arr[:n-k]))