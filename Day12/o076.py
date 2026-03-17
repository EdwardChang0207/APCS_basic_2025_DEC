n = int(input())
h = list(map(int, input().split()))
p_max = 0
p = 1
for i in range(1,len(h)):
    if h[i] < h[i-1]: p += 1
    else:
        if p > p_max: 
            p_max = p
        p = 1
if p > p_max: 
    p_max = p
print(p_max)