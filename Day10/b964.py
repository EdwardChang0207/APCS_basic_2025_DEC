n = int(input())
s = list(map(int, input().split()))

s.sort()
print(*s) #* for all -> print(s[0],s[1], ....)

if s[-1] < 60:#worst
    print(s[-1])
    print('worst case')
elif s[0] >= 60:#best
    print('best case')
    print(s[0])
else: #normal 
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break