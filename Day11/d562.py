import sys
for n in sys.stdin:
    n = int(n)
    l = input().split()
    print(*l)
    for i in range(n-1):
        l.pop(0)
        l.reverse()
        print(*l)