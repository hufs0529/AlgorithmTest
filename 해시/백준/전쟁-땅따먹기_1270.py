n = int(input())
lst = []
for _ in range(n):
    dic = dict()
    nums = list(map(int, input().split()))
    num = nums[0]
    del nums[0]
    for i in range(num):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    
    max_value = max(dic.values())
    max_key = max(dic, key=lambda x:dic[x])
    if max_value > num//2:
        lst.append(max_key)
    else:
        lst.append("SYJKGW")

for l in lst:
    print(l)