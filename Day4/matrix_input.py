m, n = map(int, input().split())
'''
l = []
for i in range(m):
    row = list(map(int, input().split()))
    l.append(row)
'''

l = [list(map(int, input().split())) for _ in range(m)]
print(l)