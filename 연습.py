from itertools import combinations

while True:
    n, k = map(int, input().split())
    
    arr = [i for i in range(1, n+1)]
    
    #print(list(map(''.join(combinations(arr, k)))))
    print()