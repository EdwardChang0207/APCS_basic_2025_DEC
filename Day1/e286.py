k = 0 #21點 7=0 7>=1 7<=-1
#*2
for i in range(2):
    #處理一局的方式
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f'{sum(a)}:{sum(b)}')
    if sum(a) > sum(b): k += 1
    else: k -= 1

if k > 0: print('Win')
elif k == 0: print('Tie')
else: print('Lose')