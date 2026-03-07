n = int(input())

def m(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

p = [list(map(int, input().split())) for _ in range(n)]

d_max, d_min = m(p[0][0], p[0][1], p[1][0], p[1][1]), m(p[0][0], p[0][1], p[1][0], p[1][1])
for i in range(n-1):
    d = m(p[i][0], p[i][1], p[i+1][0], p[i+1][1])
    if d > d_max: d_max = d
    if d < d_min: d_min = d

print(d_max, d_min)