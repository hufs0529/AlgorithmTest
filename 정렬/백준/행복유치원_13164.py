n, k = map(int, input().split())
kids = list(map(int, input().split()))
diff = []

for i in range(n-1):
    diff.append(kids[i+1]-kids[i])
diff.sort()

sum = 0
for i in range(n-k):
    sum += diff[i]
print(sum)