import sys
for s in sys.stdin:
    longest_char = ''
    length = 1
    c = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:#中斷
            if c > length: #找到更長的
                longest_char = s[i-1]
                length = c
            c = 0
        c += 1
    if c > length: #找到更長的
                longest_char = s[i-1]
                length = c
    print(longest_char, length)