n, m = map(int, input().split())
e = []
for i in range(n):
    l = list(map(int, input().split()))
    e.append(max(l))
s = sum(e)
print(s)
e = [i for i in e if s % i == 0]
if e:
    print(*e) #print(e[0], e[1], e[2], ...)
else:
    print(-1)