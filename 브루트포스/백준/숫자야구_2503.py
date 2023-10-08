from itertools import permutations
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
per = list(permutations(data, 3))
n = int(input())
for _ in range(n):
    num, strike, ball = map(int, input().split())
    num = list(str(num))
    cnt = 0
    for i in range(len(per)):
        s, b = 0, 0
        i -= cnt
        for j in range(3):
            if per[i][j] == num[j]:
                s += 1
            elif num[j] in per[i]:
                b += 1

        if (strike != s) or (ball != b):
            per.remove(per[i])
            cnt += 1

print(len(per))