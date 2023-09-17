from collections import Counter
words = input()
check_word = Counter(words)
cnt = 0
result = ''
mid = ''

for key, value in list(check_word.items()):
    if value %2 == 1:
        cnt += 1
        mid = key
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for key, value in check_word.items():
    result += (key * (value//2))
print(result + mid + result[::-1])