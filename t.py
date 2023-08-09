from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = [0] * (n+1)

def bfs(num):
    queue = deque()
    queue.append(num)
    while queue:
        q = queue.popleft()
        for i in tree[q]:
            if ans[i] == 0:
                ans[i] = q
                queue.append(i)

bfs(1)
res = ans[2:]
for x in res:
    print(x)