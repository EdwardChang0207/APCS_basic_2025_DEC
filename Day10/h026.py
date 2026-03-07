F = input()
N = int(input())
y = input().split()

t = False
#in:絲絲(lose), out:打敗絲絲的(win)
k = {'0':'5', '2':'0', '5':'2'}
for i in range(N):
    print(F, end=' ')
    if F == k[y[i]]: #win
        print(f': Won at round {i+1}')
        t = True
        break
    elif y[i] == k[F]: #lose
        print(f': Lost at round {i+1}')
        t = True
        break
    else:
        #0 -> -1 -> condition
        if i != 0 and y[i-1] == y[i]:
            F = k[y[i]]
        else:
            F = y[i]

if not t:
    print(f': Drew at round {N}')