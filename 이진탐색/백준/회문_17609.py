n = int(input())
words = []
for _ in range(n):
    words.append(input())

for word in words:
    left, right = 0, len(word) - 1
    if word[left] == word[right]:
        left += 1
        right -= 1
    else:
        if left < right-1:
            temp = word[:right] + word[right+1:]
            if temp[:] == temp[::-1]:
                print(1)
        if left + 1 < right:
            temp = word[:left] + word[left+1:]
            if temp[:] == temp[::-1]:
                print(1)
        print(2)
        