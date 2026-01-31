#等差數列
def a(a0, d, n):
    if n == 0: return a0
    else: return a(a0+d, d, n-1)

print(a(1,1,10))

#等比數列
def b(b0, r, n):
    if n == 0: return b0
    else: return b(b0*r, r, n-1)

print(b(1,2,3))

#等差級數
def c(a0, d, n):
    if n == 0: return a0
    else: return a(a0, d, n) + c(a0, d, n-1)

def d(a0, d, n):
    if n == 0: return a0
    else: return a0 + d(a0+d, d, n)

#等比級數
def e(b0, r, n):
    if n == 0: return b0
    else: return b(b0, r, n) + e(b0, r, n-1)

def f(b0, r, n):
    if n == 0: return b0
    else: return b0 + f(b0*r, r, n-1)

def Fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1) + Fib(n-2)

print(Fib(6))