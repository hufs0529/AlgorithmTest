def dfs(depth, start):
    global result
    if depth == len_:
        sour = 1
        bitter = 0
        for i in arr:
            sour *= i[0]
            bitter += i[1]
        if abs(sour - bitter) <result:
            result = abs(sour - bitter)
        return
    
    for i in range(start, n):
        arr.append(s[i])
        dfs(depth+1, i+1)
        arr.pop()


n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
arr = []
result = 99999
  
for i in range(1, n+1):
    len_ = i
    dfs(0, 0)
    
print(result)