from itertools import permutations

a, b = input().split()
b = int(b)
c = -1
a_list = []

for p in permutations(a):
    a_list.append("".join(p))

for i in a_list:
    if i[0] == 0:
        continue
    i = int(i)
    if i < b:
        c = max(c, i)

print(c)
