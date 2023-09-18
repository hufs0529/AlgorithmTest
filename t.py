t = int(input())
for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    result = 0
    for i in range(2, n):
        result = max(result, abs(trees[i] - trees[i-2]))
    print(result)