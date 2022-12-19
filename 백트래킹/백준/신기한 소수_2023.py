n = int(input())

def checkPrime(check_number):
    for i in range(2, int(check_number**0.5)+1):
        if int(check_number) % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num))==n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if checkPrime(temp) == True:
                dfs(temp)
                
                
dfs(2)
dfs(3)
dfs(5)
dfs(7)