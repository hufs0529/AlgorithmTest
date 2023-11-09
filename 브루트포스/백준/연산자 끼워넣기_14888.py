from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

min_val = 1e9
max_val = -1e9

def solve():
    global min_val, max_val
    for case in permutations(op, n-1):
        total = num[0]
        for r in range(1, n):
            if case[r-1] == '+':
                total += num[r]
            if case[r-1] == '-':
                total -= num[r]
            if case[r-1] == '*':
                total *= num[r]
            if case[r-1] == '/':
                total = int(total / num[r])

        if total > max_val:
            max_val = total
        if total < min_val:
            min_val = total

solve()
print(max_val)
print(min_val)