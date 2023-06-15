n, p, q = map(int, input().split())
dict = {}
dict[0] = 1

def sol(n):
  if n in dict:
    return dict[n]
  else:
    dict[n] = sol(n//p) +  sol(n//q)
    return dict[n]
  
print(sol(n))