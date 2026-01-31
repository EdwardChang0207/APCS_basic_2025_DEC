r, c, k, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(r)]
v = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(m):
    d = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if city[i][j] == -1: continue
            d_c = city[i][j] // k
            for a, b in v:
                if not(i+a in range(0, r)) or not(j+b in range(0, c)):
                    continue
                if city[i+a][j+b] == -1: continue
                d[i][j] -= d_c
                d[i+a][j+b] += d_c
    
    for i in range(r):
        for j in range(c):
            city[i][j] += d[i][j]      

p_min, p_max = city[0][0], city[0][0]
for i in range(r):
    for j in range(c):
        if city[i][j] == -1: continue
        if city[i][j] > p_max: p_max = city[i][j]
        if city[i][j] < p_min: p_min = city[i][j]
print(p_min)
print(p_max)         
