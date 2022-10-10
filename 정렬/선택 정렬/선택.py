array=[7,9,4,0,2,1,6,8,5]

for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)):
    if array[i] < array[min_index]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]
print(array)
  