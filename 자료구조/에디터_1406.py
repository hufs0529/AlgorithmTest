words = list(input())
cursor = len(words)
n = int(input())

for _ in range(n):
    s = list(input().split())
    if s[0] == 'P':
        words.insert(cursor, s[1])
        cursor += 1
        
    elif s[0] == 'L':
        if cursor > 0:
            cursor -= 1
            
    elif s[0] == 'D':
        if cursor < len(words):
            cursor += 1
            
    else:
        if cursor > 0:
            words.remove(words[cursor-1])
            
print(''.join(words))