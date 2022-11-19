n = int(input())
vote = int(input())
students = list(map(int, input().split()))
picture, score = [], []

for i in range(vote):
  if students[i] in picture:
    for j in range(len(picture)):
      if students[i] == picture[j]:
        score[j] += 1
  
  else:
    if len(picture) >= n:
      for j in range(n):
        if score[j] == min(score):
          del score[j]
          del picture[j]
          break
    score.append(1)
    picture.append(students[i])
    
picture.sort()
print(' '.join(map(str, picture)))