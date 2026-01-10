m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
AT = []
for i in range(n):
    r = []
    for j in range(m):
        r.append(A[j][i])
    AT.append(r)
print(*AT, sep='\n')
