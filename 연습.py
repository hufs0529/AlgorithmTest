from 브루트포스.백준.트럭_133335 import L


n = int(input())
s = []
maxH = 1
maxL = 0
maxIndex = 0
for _ in range(n):
  a, b = map(int, input().split())
  s.append([a, b])
  if maxL < a:
    maxL = a
  if maxH < b:
    maxH = b
    maxIndex = a
  
s.sort(key=lambda x:x[0])
tmpLeft = 0
tmpRight = 0
resLeft = 0
resRight = 0

for i in range(len(maxIndex, maxL+1)):
  if s[i][1] > s[-1][1]:
    tmpRight = s[i][1]
  else:
    tmpRight = maxH
  resRight = (s[i][0] - s[maxIndex][0]) * tmpRight

for i in range(len(maxIndex)-1, -1, -1):
  if s[i][1] > s[0][1]:
    tmpLeft = maxH
  else:
    tmpLeft = s[i][1]
  resLeft = () * tmpLeft
  