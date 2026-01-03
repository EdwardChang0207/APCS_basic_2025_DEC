'''
for loop: 知道跑幾次

while loop: 不知道跑幾次

for loop可以做的事 while loop也都做得到 -> O

while <condition>

for 索引值 in 範圍
for i in ['鮭魚','鮪魚','玉子燒']:
    print(i)
    if i == '鮪魚':print('take')

p = [(1, 2), (2, 5), (4, 2)]
for x, y in p:
    print(x, y)

範圍
(1) list
(2) str
(3) range(start:0, end, interval:1)
from start to end-1, increase + interval for each run
for i in range(10, 0, -1):
    print(i)
    
[list(map(int, input().split())) for i in range(3)]
l = [1, 2, 3, 4, 5]
l2 = [i for i in l if i != 3]
print(l2)

for i in range(10):
    if i == 7: break
    elif i % 2 == 0: continue
    print(i)
'''