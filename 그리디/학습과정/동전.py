array=[500,100,50,10]
M = int(input())
count = 0

for i in array:
  count+= M//i
  M%=i
print(count)


