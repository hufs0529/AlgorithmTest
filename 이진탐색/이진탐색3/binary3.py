N, K = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
b = [0] * 10
count = 0

for i in array:
  if i == K:
    count += 1
  if count == 0:
    count = -1

print(count)