def exchange(S):
    S = list(S)
    for i in range(0,len(S),2):
        S[i],S[i+1] = S[i+1], S[i]
    return S

def sorting(S):
    S = list(S)
    for i in range(0,len(S),2):
        S[i:i+2] = sorted(S[i:i+2])
    return S

def perfect_sort(S):
    result = []
    for i in range(len(S)//2):
        result.append(S[i])
        result.append(S[i+len(S)//2])
    return result

S = input()
k = int(input())

for _ in range(k):
    i = int(input())
    if i == 0:
        S = exchange(S)
    elif i == 1:
        S = sorting(S)
    else:#i==2
        S = perfect_sort(S)
print(*S,sep='')