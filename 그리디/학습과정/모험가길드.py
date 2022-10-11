N = int(input())
D = list(map(int, input().split()))
D.sort()

G = 0
C = 0

for i in D:
  C += 1
  if C >= i:
    G += 1
    C = 0

print(G)

