n = int(input())
atk = []
dfn = []
abt = []

for i in range(n):
    a, d = map(int, input().split())
    atk.append(a)
    dfn.append(d)
    abt.append(a**2+d**2)

m = abt.index(max(abt))
atk.pop(m)
dfn.pop(m)
abt.pop(m)

m = abt.index(max(abt))
print(atk[m],dfn[m])