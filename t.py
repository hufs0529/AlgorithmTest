<<<<<<< HEAD
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def pooling(size, x, y):
    mid = size // 2
    if size == 2:
        answer = [graph[x][y], graph[x+1][y], graph[x][y+1], graph[x+1][y+1]]
        answer.sort()
        return answer[-2]
    lt = pooling(mid, x, y)
    rt = pooling(mid, x + mid, y)
    lb = pooling(mid, x, y + mid)
    rb = pooling(mid, x + mid, y + mid)
    answer = [lt, rt, lb, rb]
    answer.sort()
    return answer[-2]

print(pooling(n, 0, 0))
=======

>>>>>>> a6aea9b819bd6904ff210b1e6aa48ffe4bfebd05
