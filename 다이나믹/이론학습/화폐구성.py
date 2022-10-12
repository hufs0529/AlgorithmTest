n, m = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = max(array)
cnt = 0

def binary(x):
  while left <= right:
    mid = (left + right) // 2
    global cnt
    for _ in array:
      if array - mid > 0:
        cnt += array - mid
    
      if cnt == m:
        return mid
      elif cnt > m:
        left = mid + 1
      else:
        right = mid - 1

  print(mid)

