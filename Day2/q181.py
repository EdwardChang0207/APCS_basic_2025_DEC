a, b = map(int,input().split())
people = int(input())
r = a + b
time = list(map(int,input().split()))
total = 0

for t in time:
    t %= r
    if t >= a: 
        total += (r-t)
print(total)