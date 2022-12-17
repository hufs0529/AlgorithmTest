n, m = map(int, input().split())
walk = list(map(int, input().split()))
plus_walk, minus_walk = [], []
max_walk = 0

for i in walk:
    if i > 0:
        plus_walk.append(i)
    else:
        minus_walk.append(i)
    
    if abs(i) > abs(max_walk):
        max_walk = i
        
plus_walk.sort(reverse=True)
minus_walk.sort()

walking = 0

for j in range(0, len(plus_walk), m):
    if plus_walk[j] != max_walk:
        walking += plus_walk[j]
        
for k in range(0, len(minus_walk), m):
    if minus_walk[k] != max_walk:
        walking += abs(minus_walk[k])
        
walking *=2
walking += abs(max_walk)

print(walking)