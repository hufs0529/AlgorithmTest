import sys

input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain.sort(reverse=True)
box.sort(reverse=True)

time = 0
if box[0] > crain[0]:
    print(-1)
    sys.exit()
else:
    while len(box) > 0:
        for cr in crain:
            for bo in box:
                if cr >= bo:
                    box.remove(bo)
                    break
                
    time += 1
    
print(time)