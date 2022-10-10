import sys
from  collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int, input().split())
m = int(int(input()))
s = [[] for i in range(n+1)]
result = [0 for i in range(n+1)]

def bfs(start):
  queue = deque([start])
  visit = [0 for i in range(n+1)]
  visit[start] = 1
  while queue:
    q = queue.popleft()
    for i in graph[q]:
      if visit[i] == 0:
        visit[i] = 1
        result[i] = result