a, b = map(int, input().split())
n = int(input())
r = 0
for i in range(n):
    cart = list(map(int, input().split()))
    cart.sort()
    for i in range(len(cart)):
        if cart[i] >= 0: 
            cart = cart[i::]
            #start:0 end:len(cart) interval:1
            break
        cart.remove(cart[i]*-1)
    if (a in cart) and (b in cart): r += 1
print(r)