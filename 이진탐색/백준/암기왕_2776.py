t = int(input())

for _ in range(t):
    n = int(input())
    n_s = list(map(int, input().split()))
    m = int(input())
    m_s = list(map(int, input().split()))
    n_s.sort()
    
    for num in m_s:
        if num in n_s:
            print(1)
        else:
            print(0)
    