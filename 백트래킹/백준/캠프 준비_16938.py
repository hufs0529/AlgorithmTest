from math import inf

N, L, R, X = map(int, input().split())
s = list(map(int, input().split()))
answer = 0
MIN, MAX = 0, 1
check = [False] * N


def dfs(score, idx, cnt, total_sum):
  global answer
  if cnt >= 2:
    if L <= total_sum <= R and score[MAX] - score[MIN] >= X:
      answer += 1
      
  for i in range(idx, N):
    if s[i] + total_sum <= R:
      next_score = [min(score[MIN], s[i]), max(score[MAX], s[i])]
      
      dfs(next_score, i+1, cnt+1, s[i] + total_sum)
      
dfs([inf, -inf], 0, 0, 0)
print(answer)