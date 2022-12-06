dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]
n = int(input())
answer = 1e9
total = 0
visited = [[0] * n for i in range(n)]
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))


def check(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny] == 1:
            return False
    return True

def dfs(depth):
    global answer, total
    if depth == 3:
        answer = min(answer, total)
        return
    
    for x in range(1, n-1):
        for y in range(1, n-1):
            if check(x, y):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    visited[nx][ny] = 1
                    total += s[nx][ny]
                    
                dfs(depth+1)
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    visited[nx][ny] = 0
                    total -= s[nx][ny]
                
dfs(0)
print(answer)