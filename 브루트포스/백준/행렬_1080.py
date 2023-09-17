n, m = map(int, input().split())
train = [list(map(int,list(input()))) for _ in range(n)]
test = [list(map(int,list(input()))) for _ in range(n)]


def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            train[i][j] = 1 - train[i][j]

def check():
    for i in range(n):
        for j in range(m):
            if train[i][j] != test[i][j]:
                return False
    return True

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if train[i][j] != test[i][j]:
            flip(i, j)
            cnt += 1

if check():
    print(cnt)
else:
    print("-1")