def sol(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if arr[i][j] == arr[i][j+s-1] == arr[i+s-1][j] == arr[i+s-1][j+s-1]:
                return True
    return False

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]


size = min(n, m)

for k in range(size, 0, -1):
    if sol(k):
        print(k**2)
        break