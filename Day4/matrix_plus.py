m, n = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(m)]
C = []
for j in range(m):
    row = []
    for i in range(n):
        row.append(A[j][i]+B[j][i])
    C.append(row)
print(*C, sep='\n') #* for all