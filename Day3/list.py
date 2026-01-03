'''
l = [123, True, 'hello']
#.    0.   1.     2
print(l[1])

#空串列
l = []

if l:
l = [i for i in range(10)]
print(l[0:5:1])
#l[start:end:interval] from start to end-1 increase interval
#length -> len
l = [1,2,3]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))

#maximum
def maximum(l:list):
    m = l[0]
    for i in l:
        if i > m: m = i
    return m

n items

s = 0
for i in l:
    s += i
m = max(l)
for i in range(n):

l = []
l.append(1)
l.append(2)
l.insert(1, 3)
print(l)
i = l.pop(1)#position
l.remove(1)#element
print(l, i)

t = 3
for i in range(len(l)):
    if l[i] == t:
        return i

l = [1,1,2,2,2,3,3,3,3]
print(l.count(3))
print(l.index(3))
l.reverse()
print(l)
print(sorted(l))
print(l)
'''

