t = int(input())
for _ in range(t):
  n = int(input())
  people_list = [0] * n
  for i in range(n):
    t1, t2 = map(int ,input().split())
    people_list[i] = [t1, t2]
    
  people_sorted = sorted(people_list, key = lambda x:x[0])
  hired = 1
  tmp = people_sorted[0][1]
  for i in range(1, n):
    if tmp > people_sorted[i][1]:
      hired += 1
      tmp = people_sorted[i][1]
  print(hired)