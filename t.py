from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

t = int(input())
for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
