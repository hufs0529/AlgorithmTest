n = int(input())

array = []
for _ in range(n):
  colors = list(map(str, input()))
  array.append(colors)
  
maxCount = 0

def width():
  global maxCount
  
  for k in range(n):
    countRow = 1
    for l in range(n-1):
      if array[k][l] == array[k][l+1]:
        countRow += 1
        maxCount = max(maxCount, countRow)
      else:
        countRow = 1

def height():
    for k in range(n):
        global maxCount
        
        countColumn = 1 #초기 개수를 1로 초기화
        for l in range(n - 1):
            if array[l][k] == array[l + 1][k]: #만약 같은 행의 사탕의 색이 같다면
                countColumn += 1 #사탕 개수를 1개씩 증가시켜주고
                maxCount = max(maxCount,countColumn) #증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
            else: #만약 같은 행의 색이 다르다면
                countColumn = 1 #개수를 1로 초기화

for i in range(n):
  for j in range(n-1):
    if array[i][j] != array[i][j+1]:
      array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
      width()
      height()
      