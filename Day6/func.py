'''
def matrix_plus(m, n, A, B):
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

A = [[1,2,3]]
B = [[4,5,6]]
print(matrix_plus(1,3,A,B))
'''
#區域變數 local variable/全域變數 global variable

def a():
    global n
    if n == 0: n = 2
    elif n % 2 == 0: n//=2
    else: n *= (n-1)

n = 8
a()
print(n)