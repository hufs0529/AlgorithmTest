from itertools import combinations
from collections import Counter

n = int(input())
s = list(map(int, input().split()))

sum_list = []
for i in range(1, n+1):
  com = list(combinations(s, i))
  for j in com:
    sum_list.append(sum(j))

sum_list.sort()

check_num = [i for i in range(1, sum_list[-1]+2)]

result = Counter(check_num) - Counter(sum_list)

print(list(result.keys())[0])