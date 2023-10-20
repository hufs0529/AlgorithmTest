import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phone = []
    for _ in range(n):
        num = input()
        phone.append(num)
    phone.sort()
    print(phone)
    flag = True
    for i in range(n-1):
        long = len(phone[i])
        if phone[i] == phone[i+1][:long]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")