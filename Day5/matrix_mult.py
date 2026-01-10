#Amxn Bnxk
m, n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(m)]
B = [list(map(int, input().split())) for _ in range(n)]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        t = 0
        for k in range(len(B)):
            t += A[i][k] * B[k][j]
        row.append(t)
    C.append(row)

print(*C, sep='\n')