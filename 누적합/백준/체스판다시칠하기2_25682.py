import sys
input = sys.stdin.readline
sys.maxsize
n, m, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(list(input()))
row = n-k+1
column = m-k+1

def make_chess(color):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i+j)%2 == 0:
                value = s[i][j] != color
            else:
                value = s[i][j] == color
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + value
    count = sys.maxsize

    for i in range(1, row+1):
        for j in range(1, column+1):
            count = min(count, dp[i+k-1][j+k-1] - dp[i+k-1][j-1] - dp[i-1][j+k-1] + dp[i-1][j-1])
    return count

print(min(make_chess('B'), make_chess('W')))